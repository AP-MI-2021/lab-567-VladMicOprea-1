from Tests.testCRUD import testAdaugaCarte, testStergereCarte, testModificaCartea
from Tests.testDomain import testCarte
from Tests.testFunctionalitati import testDiscount, testModificareLista


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergereCarte()
    testModificaCartea()
    testDiscount()
    testModificareLista()