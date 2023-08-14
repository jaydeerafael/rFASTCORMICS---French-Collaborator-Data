import numpy
import pandas
import cobra
import glob
import time
import scipy, scipy.signal
from pathlib import Path
from cobra.io import load_matlab_model, save_matlab_model, read_sbml_model, write_sbml_model, load_model
import logging

data_dir = Path(".") / ".." / "src" / "cobra" / "data"
data_dir = data_dir.resolve()

# Set the number of processes to use
num_processes = 96

start_time = time.time()


# Laminar_33
Laminar_33_path = data_dir / '/users/home/jdr2/test_stuff/Laminar_33.sbml.xml'
Laminar_33 = read_sbml_model(str(Laminar_33_path.resolve()))
Laminar_33_optgp = cobra.sampling.optgp.OptGPSampler(Laminar_33, processes=num_processes, thinning=100)
Laminar_33_optgp_100 = Laminar_33_optgp.sample(n=100, fluxes=True).transpose()
Laminar_33_optgp_100.to_csv('Laminar_33_optgp_k100_n100.csv')

# Laminar_90
Laminar_90_path = data_dir / '/users/home/jdr2/test_stuff/Laminar_90.sbml.xml'
Laminar_90 = read_sbml_model(str(Laminar_90_path.resolve()))
Laminar_90_optgp = cobra.sampling.optgp.OptGPSampler(Laminar_90, processes=num_processes, thinning=1000)
Laminar_90_optgp_1000 = Laminar_90_optgp.sample(n=1000, fluxes=True).transpose()
Laminar_90_optgp_1000.to_csv('Laminar_90_optgp_k1000_n1000.csv')

# Laminar_90
Laminar_90_path = data_dir / '/users/home/jdr2/test_stuff/Laminar_90.sbml.xml'
Laminar_90 = read_sbml_model(str(Laminar_90_path.resolve()))
Laminar_90_optgp = cobra.sampling.optgp.OptGPSampler(Laminar_90, processes=num_processes, thinning=100)
Laminar_90_optgp_100 = Laminar_90_optgp.sample(n=100, fluxes=True).transpose()
Laminar_90_optgp_100.to_csv('Laminar_90_optgp_k100_n100.csv')

# Oscillatory_33
Oscillatory_33_path = data_dir / '/users/home/jdr2/test_stuff/Oscillatory_33.sbml.xml'
Oscillatory_33 = read_sbml_model(str(Oscillatory_33_path.resolve()))
Oscillatory_33_optgp = cobra.sampling.optgp.OptGPSampler(Oscillatory_33, processes=num_processes, thinning=100)
Oscillatory_33_optgp_100 = Oscillatory_33_optgp.sample(n=100, fluxes=True).transpose()
Oscillatory_33_optgp_100.to_csv('Oscillatory_33_optgp_k100_n100.csv')

# Oscillatory_90
Oscillatory_90_path = data_dir / '/users/home/jdr2/test_stuff/Oscillatory_90.sbml.xml'
Oscillatory_90 = read_sbml_model(str(Oscillatory_90_path.resolve()))
Oscillatory_90_optgp = cobra.sampling.optgp.OptGPSampler(Oscillatory_90, processes=num_processes, thinning=1000)
Oscillatory_90_optgp_1000 = Oscillatory_90_optgp.sample(n=1000, fluxes=True).transpose()
Oscillatory_90_optgp_1000.to_csv('Oscillatory_90_optgp_k1000_n1000.csv')

# Oscillatory_90
Oscillatory_90_path = data_dir / '/users/home/jdr2/test_stuff/Oscillatory_90.sbml.xml'
Oscillatory_90 = read_sbml_model(str(Oscillatory_90_path.resolve()))
Oscillatory_90_optgp = cobra.sampling.optgp.OptGPSampler(Oscillatory_90, processes=num_processes, thinning=100)
Oscillatory_90_optgp_100 = Oscillatory_90_optgp.sample(n=100, fluxes=True).transpose()
Oscillatory_90_optgp_100.to_csv('Oscillatory_90_optgp_k100_n100.csv')

# Static_33
Static_33_path = data_dir / '/users/home/jdr2/test_stuff/Static_33.sbml.xml'
Static_33 = read_sbml_model(str(Static_33_path.resolve()))
Static_33_optgp = cobra.sampling.optgp.OptGPSampler(Static_33, processes=num_processes, thinning=100)
Static_33_optgp_100 = Static_33_optgp.sample(n=100, fluxes=True).transpose()
Static_33_optgp_100.to_csv('Static_33_optgp_k100_n100.csv')

# Static_90
Static_90_path = data_dir / '/users/home/jdr2/test_stuff/Static_90.sbml.xml'
Static_90 = read_sbml_model(str(Static_90_path.resolve()))
Static_90_optgp = cobra.sampling.optgp.OptGPSampler(Static_90, processes=num_processes, thinning=1000)
Static_90_optgp_1000 = Static_90_optgp.sample(n=1000, fluxes=True).transpose()
Static_90_optgp_1000.to_csv('Static_90_optgp_k1000_n1000.csv')

# Static_90
Static_90_path = data_dir / '/users/home/jdr2/test_stuff/Static_90.sbml.xml'
Static_90 = read_sbml_model(str(Static_90_path.resolve()))
Static_90_optgp = cobra.sampling.optgp.OptGPSampler(Static_90, processes=num_processes, thinning=100)
Static_90_optgp_100 = Static_90_optgp.sample(n=100, fluxes=True).transpose()
Static_90_optgp_100.to_csv('Static_90_optgp_k100_n100.csv')

end_time = time.time()

total_time = end_time - start_time

# Print the total time taken
print(f"Total time taken: {total_time:.2f} seconds")
