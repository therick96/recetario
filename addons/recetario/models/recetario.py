# -*- coding: UTF-8 -*-

from odoo import fields, models, api

class Busqueda (models.AbstractModel): #Para buscar recetas
    _name = 'recetario.busqueda'

    busqueda = fields.Char('Buscar Receta')
    recetas_ids = fields.One2many('recetario.receta','busqueda_id', string="Recetas")

class Recetas (models.Model): #Recetas
    _name = 'recetario.receta'

    name = fields.Char('Título')
    imagen = fields.Binary('Imagen')
    preparacion = fields.Text('Procedimiento')
    autor_ids = fields.Many2many('recetario.autor', string="Autor")
    ingredientes_ids = fields.Many2many('recetario.ingredientes', string="Ingredientes")
    utencilios_ids = fields.Many2many('recetario.utencilios', string="Utencilios")
    tipo_ids = fields.Many2many('recetario.tipo_comida', string="Tipo de Receta")

    busqueda_id = fields.Many2one('recetario.busqueda')


class Autores (models.Model): #Autores de las recetas
    _name = 'recetario.autor'

    name = fields.Char('Nombre')
    gender = fields.Selection([('M','M'),('F','F')], 'Género')
    nacionalidad_id = fields.Many2one('res.country','Nacionalidad')
    especialidad = fields.Char('Especialidad')
    recetas_ids = fields.One2many('recetario.receta','autor_ids', string="Recetas")


class TipoComida (models.Model): #Tipos de Recetas
    _name = 'recetario.tipo_comida'

    categoria = fields.Char('Categoria')
    estilo = fields.Char('Estilo')
    recetas_ids = fields.One2many('recetario.receta', 'tipo_ids', string="Recetas")


class Ingredientes (models.Model): #Ingredientes para las recetas
    _name = 'recetario.ingredientes'

    name = fields.Char('Nombre')
    tipo = fields.Char('Tipo')
    recetas_ids = fields.One2many('recetario.receta', 'tipo_ids', string="Recetas")


class Utencilio (models.Model): #Utencilios para las recetas
    _name = 'recetario.utencilios'

    name = fields.Char('Nombre')
    tipo = fields.Char('Tipo')
    uso = fields.Char('Uso')
    recetas_ids = fields.One2many('recetario.receta', 'tipo_ids', string="Recetas")


class Unidad (models.Model): #Unidades de medida
    _name = 'recetario.ingredientes.unidad'

    medida = fields.Char('Sistema de medida')
    descripcion = fields.Text('Descripción')
    categoria = fields.Char('Categoria')


class RecetaIngrediente (models.Model): #Modelo intermedio entre receta e ingredientes
    _name = 'recetario.receta_ingrediente'

    cantidad = fields.Integer('Cantidad')