# -*- coding: utf-8 -*-

'''
***///*** === Area de Influencia para Oleoductos === ***///*** 
Area_influencia_oleoducto
Created on: 2019-12-07 01:52:24.00000
By: Marco Portillo
'''

# Import arcpy module
import arcpy


# Script arguments
Seleccione_un_oleoducto = arcpy.GetParameterAsText(0)
if Seleccione_un_oleoducto == '#' or not Seleccione_un_oleoducto:
    Seleccione_un_oleoducto = "Oleoducto" # provide a default value if unspecified

expression = arcpy.GetParameterAsText(1)
if expression == '#' or not expression:
    expression = "Name = 'Ares'" # provide a default value if unspecified

Valor_inicial = arcpy.GetParameterAsText(2)
if Valor_inicial == '#' or not Valor_inicial:
    Valor_inicial = "50" # provide a default value if unspecified

Valor_final = arcpy.GetParameterAsText(3)
if Valor_final == '#' or not Valor_final:
    Valor_final = "150" # provide a default value if unspecified

factor_de_incremento = arcpy.GetParameterAsText(4)
if factor_de_incremento == '#' or not factor_de_incremento:
    factor_de_incremento = "50" # provide a default value if unspecified

Oleo__Value_m = arcpy.GetParameterAsText(5)
if Oleo__Value_m == '#' or not Oleo__Value_m:
    Oleo__Value_m = "C:\\Users\\Marco\\Documents\\Proyectos Geomáticos\\Proy Model Builder\\Proy MB.gdb\\Oleo_%Value%m" 

Ecoregiones_vzla_Clip = arcpy.GetParameterAsText(6)
if Ecoregiones_vzla_Clip == '#' or not Ecoregiones_vzla_Clip:
    Ecoregiones_vzla_Clip = "C:\\Users\\Marco\\Documents\\Proyectos Geomáticos\\Proy Model Builder\\Proy MB.gdb\\Ecoregiones_vzla_Clip" 

# Local variables:
Eco_regiones_vzla = "Eco_regiones_vzla"
Oleo_select = "C:\\Users\\Marco\\Documents\\ArcGIS\\Default.gdb\\Oleo_select"
Value = Valor_inicial
Dissolve_Type = "NONE"
Ecoregiones_vzla_Clip__3_ = Ecoregiones_vzla_Clip

# Process: Select
arcpy.Select_analysis(Seleccione_un_oleoducto, Oleo_select, expression)

# Process: For
arcpy.IterateCount_mb(Valor_inicial, Valor_final, factor_de_incremento)

# Process: Buffer
arcpy.Buffer_analysis(Oleo_select, Oleo__Value_m, Value, "FULL", "ROUND", Dissolve_Type, "", "PLANAR")

# Process: Clip
arcpy.Clip_analysis(Eco_regiones_vzla, Oleo__Value_m, Ecoregiones_vzla_Clip, "")

# Process: Calculate Field
arcpy.CalculateField_management(Ecoregiones_vzla_Clip, "Hectareas", "!shape.area@hectares!", "PYTHON_9.3", "")


print "***///Script Finalizado///***"
print "***/////Check results/////***"


