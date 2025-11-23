from odoo import models, fields, api

class ServerLogEventHistory(models.Model):
    _name = 'server.log.event.history'
    _description = 'Server Log Event History'

    name = fields.Char('Event', required=True)
    user_id = fields.Many2one(
        'res.users',
        string='User',
        default=lambda self: self.env.user,
        required=True
    )

    _sql_constraints = [
        (
            'unique_event_per_user',
            'UNIQUE(name, user_id)',
            'This event already exists for this user!'
        )
    ]

    @api.model
    def get_user_events(self):
        #Return a list of event names previously used by the current user.
        return self.search([
            ('user_id', '=', self.env.user.id)
        ]).mapped('name')