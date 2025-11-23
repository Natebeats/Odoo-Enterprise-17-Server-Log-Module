from odoo import models, fields, api

class ServerLog(models.Model):
    _name = 'server_log'
    _description = 'Server Log Entry'

   
    location = fields.Char('Wo', required=True)

    # Replace event Char with a Many2one to the history model
    event_id = fields.Many2one(
        'server.log.event.history',
        string='Was',
        required=True,
        help='Select an existing event or create a new one.'
    )

    start = fields.Datetime('Start', default=fields.Datetime.now, required=True)
    end = fields.Datetime('Ende')
    user_id = fields.Many2one(
        'res.users',
        string='Wer',
        default=lambda self: self.env.user,
        required=True
    )
    comment = fields.Text('Kommentar')
