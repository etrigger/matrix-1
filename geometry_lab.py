from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    from matutil import identity
    return identity(labels,1)

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    M = identity()  
    M[('x','u')] = x
    M[('y','u')] = y  
    return M
    
## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    M = identity() 
    M[('x','x')] = a
    M[('y','y')] = b  
    return M

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    from math import sin,cos
    M = identity()
    M[('x','x')] = cos(angle)
    M[('y','y')] = cos(angle)
    M[('y','x')] = sin(angle)
    M[('x','y')] = -sin(angle)
    return M

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    
    # Auxiliar matrix to translate to the origin
    M_translate_to_origin_point = identity()
    M_translate_to_origin_point[('x','u')] = -x
    M_translate_to_origin_point[('y','u')] = -y
    
    # Auxiliar matrix to translate to the origin
    M_translate_to_original_position = identity()
    M_translate_to_original_position[('x','u')] = x
    M_translate_to_original_position[('y','u')] = y
    
    
    # Rotate the point in the origin
    matrix_rotated = rotation(angle)*M_translate_to_origin_point
    # Matrix rotated respecto point
    matrix_rotated_respect_point = M_translate_to_original_position*matrix_rotated
    return matrix_rotated_respect_point
    
## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    M = identity()
    M[('x','x')] = -1
    return M

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    M = identity()
    M[('y','y')] = -1
    return M
    
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    M = identity({'r','g','b'}) 
    M[('r','r')] = scale_r
    M[('g','g')] = scale_g 
    M[('b','b')] = scale_b
    return M


## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    M = identity({'r','g','b'}) 
    M[('r','r')] = 77/256
    M[('r','g')] = 151/256 
    M[('r','b')] = 28/256
    
    M[('g','r')] = 77/256
    M[('g','g')] = 151/256
    M[('g','b')] = 28/256 
    
    M[('b','r')] = 77/256
    M[('b','g')] = 151/256
    M[('b','b')] = 28/256
    return M
  

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


