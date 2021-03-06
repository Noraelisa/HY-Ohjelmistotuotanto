import unittest
from ostoskori import Ostoskori
from tuote import Tuote

MAITO_HINTA = 3
MEHU_HINTA = 2

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.mehu = Tuote("Mehu", 2)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), MAITO_HINTA)

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito) 
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2) 

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito) 
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito) 
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)     

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_2x_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito) 
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(self.kori.ostoskori), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote, self.maito) 
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisays_ostoskorissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito) 
        self.kori.lisaa_tuote(self.mehu)
        self.assertEqual(self.kori.tavaroita_korissa(), 2) 

    #puuttuu test11-13

    def test_jos_koriin_lisatty_tuote_poistetaan_niin_kori_on_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito) 
        self.kori.lisaa_tuote(self.mehu)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)   