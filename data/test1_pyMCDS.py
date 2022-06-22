from pyMCDS import pyMCDS

mcds = pyMCDS('output00000032.xml', '.')

print(mcds.data['discrete_cells'].keys())
print("current_phase min,max= ",mcds.data['discrete_cells']['current_phase'].min(),mcds.data['discrete_cells']['current_phase'].max())
print("x range: ",mcds.data['discrete_cells']['position_x'].min(), mcds.data['discrete_cells']['position_x'].max())
print("y range: ",mcds.data['discrete_cells']['position_y'].min(), mcds.data['discrete_cells']['position_y'].max())
print("attack_rates_0 min,max= ",mcds.data['discrete_cells']['attack_rates_0'].min(), mcds.data['discrete_cells']['attack_rates_0'].max())
