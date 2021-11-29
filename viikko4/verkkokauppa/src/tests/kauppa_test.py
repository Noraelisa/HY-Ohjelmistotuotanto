import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

def varasto_saldo(tuote_id):
    if tuote_id == 1:
        return 10
    if tuote_id == 2:
        return 5    

def varasto_hae_tuote(tuote_id):
    if tuote_id == 1:
        return Tuote(1, "maito", 5)
    if tuote_id == 2:
        return Tuote(2, "leipä", 4)

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilisiirto_metodia_kutsuessa_oikealla_asiakkaalla_tilinro_ja_summalla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 5)  

    def test_koriin_lisataan_kaksi_eri_tuotetta_varmista_tilisiirto_metodin_asiakas_tilinro_summa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 9) 

    def test_koriin_lisataan_kaksi_samaa_tuotetta_varmista_tilisiirto_metodin_asiakas_tilinro_summa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 10)

    def test_koriin_lisataan_kaksi_tuotetta_joista_toinen_loppu_varmista_tilisiirto_metodin_asiakas_tilinro_summa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 9)

    def test_aloita_asiointi_metodin_kutsuminen_nollaa_edelliset_ostokset(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)

        self.assertEqual(self.kauppa._ostoskori.hinta(), 4)

