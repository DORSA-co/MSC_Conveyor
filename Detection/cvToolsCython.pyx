import time
import numpy
cimport numpy
cimport cython
from libc.math cimport cos
from libcpp cimport bool
cdef float pi = 3.14159


ctypedef numpy.int32_t DTYPE_int32
ctypedef numpy.uint8_t DTYPE_uint8
ctypedef numpy.float32_t DTYPE_float32


@cython.boundscheck(False)
@cython.wraparound(False)
def extract_points_slope(numpy.ndarray[DTYPE_uint8, ndim=2] img, float gain_thresh, int thresh,  int min_neighbors):  

    cdef long int total_sum = 0
    cdef long int weights_sum = 0
    cdef int x,y,k
    cdef int img_h = img.shape[0]
    cdef int img_w = img.shape[1]
    cdef bint have_enough_neighbors = False
    cdef float res_y = 0
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res_pts = numpy.zeros( (img_w, 2), dtype = numpy.int32 )    
    cdef int top_y, bottom_y
    cdef float gain = 0
    cdef int win = 30

    for x in range(img_w):
        total_sum = 0
        weights_sum = 0

        bottom_y = -1
        top_y = -1

        for y in range(win, img_h - win):
            if top_y < 0:
                gain  = (img[y ,x] / (img[y-win,x]+1))

                if gain >= gain_thresh and img[y,x] >= thresh:
                    have_enough_neighbors = True

                    for k in range(1, min_neighbors + 1):
                        gain  = (img[y+k ,x] / (img[y-win,x]+1))
                        if gain < gain_thresh or img[y,x] < thresh:
                            have_enough_neighbors = False
                            break 

                    if have_enough_neighbors:  
                        top_y = y
                        total_sum += ( img[y, x] * y )
                        weights_sum += img[y, x]

            elif top_y > 0 and bottom_y < 0:
                gain  = (img[y ,x] / (img[y+win,x]+1))
                if  gain >= gain_thresh:  
                    break 


        res_pts[x][0] = x

        if weights_sum > 0:
            res_y = total_sum / weights_sum 
            res_pts[x][1] = int(res_y)

        else:
            res_pts[x][1] = -1

            
    return res_pts





@cython.boundscheck(False)
@cython.wraparound(False)
def extract_points_maxwin(numpy.ndarray[DTYPE_uint8, ndim=2] img, int thresh,  int window_size, int replacement):  

    cdef int total_y_sum = 0
    cdef int weights_sum = 0
    cdef int max_windown_conv = -1
    cdef int window_conv = 0
    cdef int max_win_idx = 0
    cdef int x,y,k
    cdef int res_y = 0
    cdef int img_h = img.shape[0]
    cdef int img_w = img.shape[1]
    
    
    cdef numpy.ndarray[DTYPE_int32, ndim=2] res_pts = numpy.zeros( (img_w, 2), dtype = numpy.int32 )    


    for x in range(0,img_w):
        max_win_idx = -1
        max_windown_conv = -1
        for y in range(0, img_h - window_size,2):
            window_conv = 0
            if img[y + window_size//2, x] > thresh:
                for k in range(0, window_size):
                    window_conv += img[y + k,x]
                
                if window_conv > max_windown_conv:
                    max_win_idx = y
                    max_windown_conv  = window_conv
        
        
        if max_win_idx > 0:
            total_y_sum = 0
            weights_sum = 0

            for k in range(0, window_size):
                y = max_win_idx + k
                total_y_sum += ( img[y, x] * y )
                weights_sum += img[y, x]


        # 

        if weights_sum > 0:
            res_y = int(total_y_sum / weights_sum )
        else:
            res_y = replacement
        
        res_pts[x, 0] = x
        res_pts[x, 1] = res_y
            
    return res_pts


@cython.boundscheck(False)
@cython.wraparound(False)
def extract_defects(numpy.ndarray[DTYPE_int32, ndim=2] error_ys, int min_width):

    cdef int start_idx = -1
    cdef int end_idx = -1
    cdef int i = 0
    cdef int defect_count = 0
    cdef int pts_count = error_ys.shape[0]

    cdef numpy.ndarray[DTYPE_int32, ndim=2] res_defect_indices = numpy.zeros( (pts_count, 3), dtype = numpy.int32 )    


    for i in range(0, pts_count):
        if start_idx<0:
            if error_ys[i, 1] != 0:
                start_idx = i
        else:
            if error_ys[i,1] == 0:
                if (i - start_idx - 1) > min_width:
                    res_defect_indices[defect_count, 0] = start_idx
                    res_defect_indices[defect_count, 1] = i
                    res_defect_indices[defect_count, 2] = 0
                    defect_count += 1
                start_idx = -1
    
    # return res_defect_indices
    return res_defect_indices[:defect_count]