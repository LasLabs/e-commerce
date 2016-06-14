# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import mock
from openerp.tests.common import TransactionCase
from openerp.addons.website_sale_default_country.controllers.main import (
    WebsiteSale
)


parent = 'openerp.addons.website_sale.controllers.main'
child = 'openerp.addons.website_sale_default_country.controllers.main'


class TestMain(TransactionCase):

    @mock.patch('%s.website_sale' % parent)
    def setUp(self, mk):
        super(TestMain, self).setUp()
        self.mock = mk
        self.controller = WebsiteSale()
        self.expect_data = {'data': 'Test'}

    def test_checkout_values_calls_super(self):
        """ It should call send data to super method """
        self.controller.checkout_values(self.expect_data)
        self.mock.checkout_values.assert_called_once_with(self.expect_data)

    @mock.patch('%s.request' % child)
    def test_checkout_values_sets_default(self, mk):
        """ It should set default of result checkout to company country """
        mk.website.company_id = self.env.ref('base.us')
        self.controller.checkout_values(self.expect_data)
        self.mock.checkout_values()['checkout'].setdefault.\
            assert_called_once_with(
                "country_id", self.env.ref('base.us').id
            )
