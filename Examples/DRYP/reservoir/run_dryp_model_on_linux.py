#cd /user/home/km19051/DRYPv2.0_test/ 
#source /user/home/km19051/miniconda3/bin/activate 
#python /user/home/km19051/WS/aux_WG_MC_Analysis.py

# Import libraries from local repository
import sys
#sys.path.append('C:/Users/Edisson/Documents/GitHub/DRYPv2.0.1')
sys.path.append('/home/andresqm/github/DRYPv2.0.1')
#sys.path.append("/home/km19051/DRYPv2.0.1")
#from context import dryp
from dryp.main_DRYP import run_DRYP

#import dryp.components.DRYP_watershed as ppbasin
import tools.DRYP_pptools as pptools
import tools.DRYP_rrtools as rrtools

#fname = "../Lake/input/LA_dem.asc"
#fname_out = "../Lake/input/LA_flowdir.asc"
#rrtools.create_raster_flowdirection_dryp(fname, fname_out, transform=False)
#fname = "HAD_IMERGa_Lake_input_sim.dmp"
fname = "LA_input.dmp"
run_DRYP(fname)