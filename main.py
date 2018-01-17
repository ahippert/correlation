#!/usr/bin/env python

import numpy as np
import gamma_to_py as gapy
import corr_zncc as zncc

def main():
    
    FILE_M = '/home/hipperta/nas_mastodons/hipperta/images/20171106.mli'
    FILE_SL = '/home/hipperta/nas_mastodons/hipperta/images/20171118.mli'
    imageFormat = 'mli'
    COL = 6468

    # 9x6 matrix representing positions around similarity peak
    # goes from P(-1,-1) to P(1,1)
    interpolationMatrix = np.matrix([[1, 1, 1, -1, -1, 1],
                                     [0, 1, 0, 0, -1, 1],
                                     [1, 1, -1, 1, -1, 1],
                                     [1, 0, 0, -1, 0, 1],
                                     [0, 0, 0, 0, 0, 1],
                                     [1, 0, 0, 1, 0, 1],
                                     [1, 1, -1, -1, 1, 1],
                                     [0, 1, 0, 0, 1, 1],
                                     [1, 1, 1, 1, 1, 1]])
    
    coefficientMatrix = np.matrix([None, None, None, None, None, None])
    
    #corr_window = 15 # half correlation window size
    #research_window = 17 # half research window size
    corr_window = 15
    research_window = 17
    
    # area of study coordinates

    # mer de glace
    line_start = 880
    col_start = 760
    #line_width = 70
    #col_width = 130

    # test
    line_width = 70
    col_width = 130
    
    master1D = gapy.ouvrir(FILE_M, imageFormat) # get images from gamma_to_py.py
    slave1D = gapy.ouvrir(FILE_SL, imageFormat)
    print('shape of former master file: %s' %master1D.shape)
    print('shape of former slave file: %s' %slave1D.shape)
    
    masterImage = gapy.reshape(master1D, COL) # reshape images
    slaveImage = gapy.reshape(slave1D, COL)
    print('master new shape: (%s,%s)' %(masterImage.shape[0],masterImage.shape[1]))
    print('slave new shape: (%s,%s)' %(slaveImage.shape[0],slaveImage.shape[1]))

    zncc.correlation_ZNCC(masterImage, slaveImage, corr_window, research_window, line_start, col_start, line_width, col_width, interpolationMatrix, coefficientMatrix)
    #zncc_matrix2D = gapy.reshape(zncc_matrix1D, COL)

    
if __name__ == '__main__':
    main()
    


