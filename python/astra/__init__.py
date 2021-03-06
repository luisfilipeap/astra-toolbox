# -----------------------------------------------------------------------
# Copyright: 2010-2016, iMinds-Vision Lab, University of Antwerp
#            2013-2016, CWI, Amsterdam
#
# Contact: astra@uantwerpen.be
# Website: http://www.astra-toolbox.com/
#
# This file is part of the ASTRA Toolbox.
#
#
# The ASTRA Toolbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The ASTRA Toolbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the ASTRA Toolbox. If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------

from . import matlab as m
from .creators import astra_dict,create_vol_geom, create_proj_geom, create_backprojection, create_sino, create_reconstruction, create_projector,create_sino3d_gpu, create_backprojection3d_gpu
from .functions import data_op, add_noise_to_sino, clear, move_vol_geom
from .extrautils import clipCircle
from . import data2d
from . import astra
from . import data3d
from . import algorithm
from . import projector
from . import projector3d
from . import matrix
from . import plugin
from . import plugins
from . import log
from .optomo import OpTomo

__version__ = '1.8'

import os

if 'ASTRA_GPU_INDEX' in os.environ:
    L = [ int(x) for x in os.environ['ASTRA_GPU_INDEX'].split(',') ]
    astra.set_gpu_index(L)
