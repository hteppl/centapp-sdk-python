import json
import traceback
from abc import ABC
from enum import Enum

import requests
from requests import HTTPError

base_url = 'https://cent.app/api/v1'


class Currency(Enum):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'


class LinkType(Enum):
    NORMAL = 'normal'
    MULTI = 'multi'


class CentApp:
    """
    Represents a CentApp instance.

    :param token: The authorization token.
    """
    
    def __init__(self, token):
        self.headers = {'Authorization': f'Bearer {token}'}
    
    def bill(self):
        return Bill(self)
    
    def payment(self):
        return Payment(self)
    
    def merchant(self):
        return Merchant(self)
    
    def payout(self):
        return Payout(self)


class Section(ABC):
    """
    Abstract base class for API sections.
    """
    
    def __init__(self, app: CentApp, section: str):
        """
        Initializes the Section instance.

        :param app: The CentApp instance.
        :param section: The section name.
        """
        self._app: CentApp = app
        self._section: str = section
    
    def _request(self, method: str, endpoint: str, data=None) -> json:
        url = f'{base_url}/{self._section}/{endpoint}'
        response = requests.request(
            method,
            url,
            headers=self._app.headers,
            params=data,
            data=data)
        try:
            response.raise_for_status()
        except HTTPError:
            traceback.print_exc()
        return response.json()


class Bill(Section):
    def __init__(self, app: CentApp):
        """
        Constructs a new 'Bill' object.

        :param app: The CentApp instance.
        """
        super().__init__(app, 'bill')
    
    def create(self,
               amount: float,
               shop_id: str,
               order_id: str or None = None,
               description: str or None = None,
               link_type: LinkType = LinkType.NORMAL,
               currency_in: Currency = Currency.RUB,
               custom: str or None = None,
               payer_pays_commission: bool = True,
               name: str or None = None) -> json:
        """
        Creates a bill.

        :param amount: The amount of the bill.
        :param shop_id: The ID of the shop.
        :param order_id: The order ID (optional).
        :param description: The bill description (optional).
        :param link_type: The link type (default: LinkType.NORMAL).
        :param currency_in: The currency of the bill (default: Currency.RUB).
        :param custom: Custom data for the bill (optional).
        :param payer_pays_commission: Whether the payer pays the commission (default: True).
        :param name: The name of the bill (optional).
        :return: The JSON response.
        """
        data = {
            'amount': amount,
            'order_id': order_id,
            'description': description,
            'type': link_type.value,
            'shop_id': shop_id,
            'currency_in': currency_in.value,
            'custom': custom,
            'payer_pays_commission': int(payer_pays_commission),
            'name': name,
        }
        return self._request('POST', 'create', data)
    
    def toggle_activity(self, shop_id: str, active: bool) -> json:
        """
        Toggles the activity of a shop.

        :param shop_id: The ID of the shop.
        :param active: Whether the shop should be active or not.
        :return: The JSON response.
        """
        data = {
            'id': shop_id,
            'active': int(active),
        }
        return self._request('POST', 'toggle_activity', data)
    
    def payments(self, bill_id: str) -> json:
        """
        Retrieves the payments for a bill.

        :param bill_id: The ID of the bill.
        :return: The JSON response.
        """
        return self._request('GET', 'payments', {'id': bill_id})
    
    def search(self,
               start_date: str or None = None,
               finish_date: str or None = None,
               shop_id: str or None = None) -> json:
        """
        Searches for bills based on the provided criteria.

        :param start_date: The start date for the search (optional).
        :param finish_date: The finish date for the search (optional).
        :param shop_id: The ID of the shop to filter the search (optional).
        :return: The JSON response.
        """
        data = {}
        
        if start_date:
            data['start_date'] = start_date
        if finish_date:
            data['finish_date'] = finish_date
        if shop_id:
            data['shop_id'] = shop_id
        
        return self._request('GET', 'search', data)
    
    def status(self, bill_id: str) -> json:
        """
        Retrieves the status of a bill.

        :param bill_id: The ID of the bill.
        :return: The JSON response.
        """
        return self._request('GET', 'status', {'id': bill_id})


class Payment(Section):
    def __init__(self, app: CentApp):
        """
        Constructs a new 'Payment' object.

        :param app: The CentApp instance.
        """
        super().__init__(app, 'payment')
    
    def search(self,
               start_date: str or None = None,
               finish_date: str or None = None,
               shop_id: str or None = None) -> json:
        """
        Searches for payments based on the provided criteria.

        :param start_date: The start date for the search (optional).
        :param finish_date: The finish date for the search (optional).
        :param shop_id: The ID of the shop to filter the search (optional).
        :return: The JSON response.
        """
        data = {}
        
        if start_date:
            data['start_date'] = start_date
        if finish_date:
            data['finish_date'] = finish_date
        if shop_id:
            data['shop_id'] = shop_id
        
        return self._request('GET', 'search', data)
    
    def status(self, payment_id: str) -> json:
        """
        Retrieves the status of a payment.

        :param payment_id: The ID of the payment.
        :return: The JSON response.
        """
        return self._request('GET', 'status', {'id': payment_id})


class Merchant(Section):
    def __init__(self, app: CentApp):
        """
        Constructs a new 'Merchant' object.

        :param app: The CentApp instance.
        """
        super().__init__(app, 'merchant')
    
    def balance(self):
        """
        Retrieves the balance of the merchant.

        :return: The JSON response.
        """
        return self._request('GET', 'balance')


class Payout(Section):
    def __init__(self, app: CentApp):
        """
        Constructs a new 'Payout' object.

        :param app: The CentApp instance.
        """
        super().__init__(app, 'payout')
    
    def personal_create(self, amount: float, payout_account_id: str):
        """
        Creates a personal payout.

        :param amount: The amount of the payout.
        :param payout_account_id: The ID of the payout account.
        :return: The JSON response.
        """
        data = {
            'amount': amount,
            'payout_account_id': payout_account_id,
        }
        return self._request('POST', 'personal/create', data)
    
    def regular_create(self, amount: float,
                       currency: Currency,
                       account_identifier: str,
                       card_holder: str):
        """
        Creates a regular payout.

        :param amount: The amount of the payout.
        :param currency: The currency of the payout.
        :param account_identifier: The identifier of the payout account.
        :param card_holder: The cardholder name for the payout.
        :return: The JSON response.
        """
        data = {
            'amount': amount,
            'currency': currency.value,
            'account_type': 'credit_card',
            'account_identifier': account_identifier,
            'card_holder': card_holder,
        }
        return self._request('POST', 'regular/create', data)
    
    def search(self,
               start_date: str or None = None,
               finish_date: str or None = None) -> json:
        """
        Searches for payouts based on the provided criteria.

        :param start_date: The start date for the search (optional).
        :param finish_date: The finish date for the search (optional).
        :return: The JSON response.
        """
        data = {}
        
        if start_date:
            data['start_date'] = start_date
        if finish_date:
            data['finish_date'] = finish_date
        
        return self._request('GET', 'search', data)
    
    def status(self, payout_id: str) -> json:
        """
        Retrieves the status of a payout.

        :param payout_id: The ID of the payout.
        :return: The JSON response.
        """
        return self._request('GET', 'status', {'payout_id': payout_id})
