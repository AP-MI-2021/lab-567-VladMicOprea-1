from Tests.testCRUD import testAdaugaCarte, testStergereCarte, testModificaCartea
from Tests.testDomain import testCarte
from Tests.testFunctionalitati import testDiscount, testModificareLista, testPretMinim, testOrdonareDupaPret, \
    testCartiCuTitluriDistincte
from Tests.testUndoRedo import testUndoRedo


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergereCarte()
    testModificaCartea()
    testDiscount()
    testModificareLista()
    testPretMinim()
    testOrdonareDupaPret()
    testUndoRedo()
    testCartiCuTitluriDistincte()