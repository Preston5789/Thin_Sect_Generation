# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import xlrd
import xlwt
import numpy as np
import sys
import os
from PIL import Image
from colorama import Fore, Back, Style 



#from StringIO import StringIO




Por = float(input("Enter Porosity (fraction) = "))
Perm = float(input("Enter Permeability (mD) = "))

print()
print(Fore.RED + "Representative Thin Section:")


# =============================================================================
# # ===========================================================================
# # #-------------------------------------------------------------------------- 
# # #                Read Spreadsheet
# # #  Read KHRS Core data which is Arab D Carbonate Data
# # #--------------------------------------------------------------------------
# # ===========================================================================
# =============================================================================


book = xlrd.open_workbook("CO3_TS_Image.xls")   #mapinv_reference cleaned up of obscure tri-modal samples
sh = book.sheet_by_index(0)


import win32com.client
o = win32com.client.Dispatch("Excel.Application")

    

Depth = []
Porosity = []
Permeability = []
Path_TS = []


    
for i in range(0,sh.nrows,1):
        Depth.append(sh.cell_value(rowx=i, colx=1))
        Porosity.append(sh.cell_value(rowx=i, colx=2))
        Permeability.append(sh.cell_value(rowx=i, colx=3))
        Path_TS.append(sh.cell_value(rowx=i, colx=4))
       
#        print(Depth[i],Porosity[i],Permeability[i],Path_TS[i])       
# =============================================================================
# # ===========================================================================
# # #--------------------------------------------------------------------------
# ##
# ##            This is the beginnin of Inverse Distance^4 
# ##
# # #--------------------------------------------------------------------------
# # ===========================================================================
# =============================================================================


#bvarray    = []; #make list of 0 length
#deptharray = []
#bvoccarray = []; #make list of 0 length


#n = int(input("Enter an integer >>>"))
#for n in range(0,1,1):        
#for n in range(400,450,1):
#    print("and wait...")
#    dep = Depth[n]

por = Por
perm= Perm
  
#print(por, perm)  
        
unc_phi=0.005
unc_lperm=0.1



dist_inv = []
dist_phi = []
dist_lperm = []

inv_dist_array = []

dist_inv_total=0

#------------------------------------------------------------------------------ 
#          Estimate Thomeer Parameters First Pore System
#------------------------------------------------------------------------------

#this is the mapinv_reference_data being used using the mapinv Porosity and Permeability vs. por and perm
for i in range(0,sh.nrows ,1):
        #compute distance and Inverse Distance for por vs Porosity[i] and perm vs Permeability[i]
        dist_phi.append(max(unc_phi,abs(por - Porosity[i])))
        dist_lperm.append(max(unc_lperm,abs(math.log10(perm) - math.log10(Permeability[i]))))
        dist_inv.append(1/(((dist_phi[i]/unc_phi)**4 + (dist_lperm[i]/unc_lperm)**4)))
        dist_inv_total = dist_inv_total +  dist_inv[i]

        inv_dist_array.append(dist_inv); #add items

#x=np.array(inv_dist_array)


a = np.array(inv_dist_array) 
inv_dist_thresh = np.percentile(a, 99.5)
#print("Inv Distance Threshold =", inv_dist_thresh)



        
for i in range(0,sh.nrows ,1):        
        if dist_inv[i] > inv_dist_thresh - 0.001:
            TS = Path_TS[i]

            print("      Reference Data: Depth =",Depth[i],", Porosity =",Porosity[i], ", Permeability =", Permeability[i],", Inv Dist '",dist_inv[i],", TS Image =", Path_TS[i])
#            print("Depth =",Depth[i]-10000,", Porosity =",Porosity[i], ", Permeability =", Permeability[i])

            img=mpimg.imread(TS)
            imgplot = plt.imshow(img)
            plt.show()
#        else:
#            print("Not Representative")
        
print(Style.RESET_ALL) 