from odoo import api, models, fields
import io
from odoo.http import request
from odoo.addons.same_motion_module.models.qr_code_base import generate_qr_code


class AccountInvoice(models.Model):
	_inherit = 'account.invoice'

	total_qty_invoice = fields.Float('Total Lines',compute='_compute_total_lines')

	sp_id = fields.Many2one('stock.picking', compute='_compute_picking')

	qr_image = fields.Binary("QR Code", compute='_generate_qr_code')

	suffix = fields.Char("CORRELATIVO", compute='_compute_invoice_number')
	prefix = fields.Char("SERIE", compute='_compute_invoice_number')
	team_id = fields.Many2one('crm.team', string='Canal de ventas')
	date_issue = fields.Datetime('Fecha de emisión',default=fields.Datetime.now , required=True)

	@api.one
	def _generate_qr_code(self):
		content = str( str(self.number) + "|" + str(self.partner_id.name) + "|" + str(self.date_invoice) + "|" + str(self.total_qty_invoice) + "|" + str(self.amount_total))
		self.qr_image = generate_qr_code(content)


	@api.one
	@api.depends('invoice_line_ids')
	def _compute_total_lines(self):
		var = 0
		if self.invoice_line_ids:
			for line in self.invoice_line_ids:
				var += line.quantity
		self.total_qty_invoice = var

	@api.one
	@api.depends('number','journal_id')
	def _compute_invoice_number(self):
		self.suffix = None
		self.prefix = None
		if self.number and self.journal_id:
			lgt = self.journal_id.sequence_id.padding
			str_number = str(self.number)
			if str_number:
				self.prefix = str_number[-lgt:]
				self.suffix = (str_number[:(len(str_number)-lgt)]).replace('/',"")

	@api.one
	def _compute_picking(self):
		self.sp_id = None
		po_id = self.env['pos.order'].search([('invoice_id','=',self.id)], limit=1)
		if po_id and po_id.picking_id:
			self.sp_id = po_id.picking_id