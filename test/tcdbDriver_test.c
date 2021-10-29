#include "general.h"
#include "ctest.h"
#include "tcdb_drivers.h"




/*****************************************************************************/
/*                       Trivial TCDB Driver TestCases                       */
/*****************************************************************************/
TcdbType trivialType = { NULL, NULL, NULL, NULL, NULL, NULL };

CTEST_DATA(TcdbDriverUT) {
  TcdbDriver *driver;
};

CTEST_SETUP(TcdbDriverUT) {
    data->driver = tcdbDriverCreate(&trivialType);
}


CTEST_TEARDOWN(TcdbDriverUT) {
    tcdbDriverRelease(data->driver);
}


CTEST2(TcdbDriverUT, Init) {}


/*****************************************************************************/
/*                         Git TCDB Driver TestCases                         */
/*****************************************************************************/
CTEST_SETUP(TcdbGitDriverUT) {
    TcdbDriver *driver;
}


CTEST_SETUP(TcdbGitDriverUT) {
    data->driver = tcdbDriverCreate(TCDB_GIT_DRIVER);
}


CTEST_TEARDOWN(TcdbGitDriverUT) {
    tcdbDriverRelease(data->driver);
}
