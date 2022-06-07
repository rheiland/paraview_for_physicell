# Sample data and scripts

```
python cells_as_glyphs.py output00000096.xml
```

Sample session with ipython:
```
In [1]: from pyMCDS_cells import pyMCDS_cells

In [2]: mcds = pyMCDS_cells('output00000032.xml', '.')

In [4]: mcds.data['discrete_cells'].keys()
Out[4]: dict_keys(['ID', 'position_x', 'position_y', 'position_z', 'total_volume', 'cell_type', 'cycle_model', 'current_phase', 'elapsed_time_in_phase', 'nuclear_volume', 'cytoplasmic_volume', 'fluid_fraction', 'calcified_fraction', 'orientation_x', 'orientation_y', 'orientation_z', 'polarity', 'migration_speed', 'motility_vector_x', 'motility_vector_y', 'motility_vector_z', 'migration_bias', 'motility_bias_direction_x', 'motility_bias_direction_y', 'motility_bias_direction_z', 'persistence_time', 'motility_reserved', 'chemotactic_sensitivities_x', 'chemotactic_sensitivities_y', 'adhesive_affinities_x', 'adhesive_affinities_y', 'dead_phagocytosis_rate', 'live_phagocytosis_rates_x', 'live_phagocytosis_rates_y', 'attack_rates_x', 'attack_rates_y', 'damage_rate', 'fusion_rates_x', 'fusion_rates_y', 'transformation_rates_x', 'transformation_rates_y', 'oncoprotein', 'elastic_coefficient', 'kill_rate', 'attachment_lifetime', 'attachment_rate', 'oncoprotein_saturation', 'oncoprotein_threshold', 'max_attachment_distance', 'min_attachment_distance'])

In [7]: mcds.data['discrete_cells']['current_phase'].min()
Out[7]: 14.0

In [8]: mcds.data['discrete_cells']['current_phase'].max()
Out[8]: 101.0
```

