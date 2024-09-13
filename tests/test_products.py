from utils import *


class TestProducts(TestBase):

    def setUp(self) -> None:
        super().setUp(filePathFromRoot="index.html")

    # Test that the products are displayed
    def testProducts(self) -> None:
        self.assertInText("Bröllopsbukett")
        self.assertInText("Rosor 10-pack")
        self.assertInText("Tulpaner 10-pack")
        self.assertInText("Sommarbukett")
        self.assertInText("Höstbukett")
        self.assertInText("Begravningskrans")

    # Test that the product prices are displayed
    def testPrices(self) -> None:
        self.assertInText("1 200 kr")
        self.assertInText("150 kr")
        self.assertInText("100 kr")
        self.assertInText("200 kr")
        self.assertInText("400 kr")
        self.assertInText("800 kr")

    # Test that the product images are displayed
    def testImages(self) -> None:
        self.assertInHTML('<img src="images/brollopsbukett.jpg" alt="bröllopsbukett">')
        self.assertInHTML('<img src="images/rosor-10-pack.jpg" alt="rosor 10-pack">')
        self.assertInHTML('<img src="images/tulpanbukett.jpg" alt="tulpaner 10-pack">')
        self.assertInHTML('<img src="images/sommarbukett.jpg" alt="sommarbukett">')
        self.assertInHTML('<img src="images/hostbukett.jpg" alt="höstbukett">')
        self.assertInHTML('<img src="images/begravningskrans.jpg" alt="begravningskrans">')


if __name__ == "__main__":
    unittest.main(verbosity=2)
