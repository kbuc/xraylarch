#
#
__DOC__ = """
Functions for accessing and using data from X-ray Databases and
Tables.  Many of these take an element as an argument -- this
can be either the atomic symbol or atomic number Z.

The data and functions here include (but are not limited to):

member name     descrption
------------    ------------------------------
materials       dictionary of composition of common materials
chemparse       parse a Chemical formula to compositiondictionary.
atomic_mass     return atomic mass for an element
f0              Thomson X-ray scattering factor
f1f2_cl         Anomalous scattering factors from Cromer-Libermann
mu_elam         X-ray attenuation coefficients from Elam etal
mu_chantler     X-ray attenuation coefficients from Chantler
xray_edges      X-ray absorption edges for an element
xray_lines      X-ray emission lines for an element
"""

from .xraydb import XrayDB as xrayDB

from .xray import (atomic_mass, atomic_number, atomic_symbol,
                   atomic_density, xray_line, xray_lines, xray_edge,
                   xray_edges, ck_probability, f0, f0_ions, mu_elam,
                   mu_chantler, f1_chantler, f2_chantler, core_width,
                   chantler_data, chantler_energies, guess_edge,
                   get_xraydb, xray_delta_beta,
                   coherent_cross_section_elam,
                   incoherent_cross_section_elam,
                   fluo_yield
                   )

from .materials import (material_get, material_add, material_mu,
                        material_mu_components, get_materials)
from .cromer_liberman import f1f2 as f1f2_cl
from .background import XrayBackground
from .chemparser import chemparse


_larch_builtins = dict(chemparse=chemparse,
                        material_get=material_get,
                        material_add=material_add,
                        material_mu=material_mu,
                        material_mu_components=material_mu_components,
                        f1f2_cl=f1f2_cl,
                        f0=f0,
                        f0_ions=f0_ions,
                        chantler_energies=chantler_energies,
                        chantler_data=chantler_data,
                        f1_chantler=f1_chantler,
                        f2_chantler=f2_chantler,
                        mu_chantler=mu_chantler,
                        mu_elam=mu_elam,
                        coherent_xsec=coherent_cross_section_elam,
                        incoherent_xsec=incoherent_cross_section_elam,
                        atomic_number=atomic_number,
                        atomic_symbol=atomic_symbol,
                        atomic_mass=  atomic_mass,
                        atomic_density=atomic_density,
                        xray_edges=xray_edges,
                        xray_edge=xray_edge,
                        xray_lines=xray_lines,
                        xray_line=xray_line,
                        fluo_yield=fluo_yield,
                        core_width= core_width,
                        guess_edge= guess_edge,
                        ck_probability=ck_probability,
                        xray_delta_beta=xray_delta_beta)

def _larch_init(_larch):
    """initialize xraydb"""
    xdb = get_xraydb(_larch)
    get_materials(_larch)
    _larch.symtable._xray.__doc__ = MODDOC
