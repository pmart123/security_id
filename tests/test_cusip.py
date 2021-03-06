from unittest import TestCase
import pytest
from cymbology import Cusip, cusip_from_isin
from cymbology.exceptions import CountryCodeError, IdError
from tests.fixtures import AlphaNumericIdMixin


class TestCusip(AlphaNumericIdMixin, TestCase):
    length_issue = ['30303M1024']
    character_issue = ['03783*100']
    check_digit_issue = ['30303M10#']
    checksum_issue = ['30303M103']

    numeric_ids = ['037833100', '37833100']
    character_ids = ['30303M102']

    valid_id = '30303M102'
    invalid_id = ""

    checksum_param = {'sid_': '03783310', 'sid': '037833100'}

    def setUp(self):
        self.obj = Cusip()

    def test_country_code_error(self):
        self.assertRaises(CountryCodeError, self.obj.validate, 'I0303M109')

    def tearDown(self):
        del self.obj


@pytest.mark.parametrize('input,expected',
                         [('US0378331005', '037833100'), ('US66987V1098', '66987V109')])
def test_cusip_from_isin(input, expected):
    assert cusip_from_isin(input) == expected


def test_cusip_from_isin_country_error():
    with pytest.raises(CountryCodeError):
        assert cusip_from_isin('ES0109067019')


def test_cusip_from_isin_validation_error():
    with pytest.raises(IdError):
        assert cusip_from_isin('USROUTE66')
