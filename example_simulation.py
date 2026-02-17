from Wave_1 import Wave as central_simulation #as seen in the "Wave_x.py" files to import you use filename-not-as-a-string and without the file extension
from Wave_2 import Wave as stochastic_simulation
from Wave_3 import Wave as alternating_simulation

seed = []
batch_names = []
STDP_scaling_factor = []

#quick test code
seed = [123, 456, 789]
batch_names = ["central", "stochastic", "alternating"] #do need to make these folders yourself beforehand b/c "Wave_x.py" files don't explicitly check for whether folder exists? And not sure np.save works if the folder doesn't exist
STDP_scaling_factor = [1, 0.8, 1.2]

for i in range(0, 2):
    central_simulation(seed[i], batch_names[0], STDP_scaling_factor[i]) #can use same batch name for different trials as long as seed changes b/c filename is batch_name + seed + filetype
    stochastic_simulation(seed[i], batch_names[1], STDP_scaling_factor[i])
    alternating_simulation(seed[i], batch_names[2], STDP_scaling_factor[i])