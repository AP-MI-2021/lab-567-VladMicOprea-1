from Tests.testCRUD import testAdaugaCarte, testStergereCarte, testModificaCartea
from Tests.testDomain import testCarte


def runAllTests():
    testCarte()
    testAdaugaCarte()
    testStergereCarte()
    testModificaCartea()