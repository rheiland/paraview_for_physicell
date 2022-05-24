$$\frac{ \partial \boldsymbol{\rho}}{\partial t} = \mathbf{D} \circ \nabla^2 \boldsymbol{\rho} - \boldsymbol{\lambda} \circ \boldsymbol{\rho} + \sum_i \delta \left( \mathbf{x} - \mathbf{x}_i \right) \Bigl[ V_i \mathbf{S}_i \circ \left( \boldsymbol{\rho}^*_i - \boldsymbol{\rho} \right) - V_i \mathbf{U}_i \circ \boldsymbol{\rho} + \mathbf{E}_i \Bigr],$$ where

col A | col B
|---| ---|
$\rho$ |  vector of densities


  |          Symbol          |      Meaning                                      |       Dimensions|
  |--------------------------| --------------------------------------------------| ------------------|
  | $\rho$        |  vector of substrate densities (or concentrations)|   substance/volume|
  |       $\mathbf{D}$       |  vector of diffusion coefficients                 |   length$^2$/time|
  |  $\boldsymbol{\lambda}$  |  vector of decay rates                            |   1/time|
