#include "unity.h"
#include "utilities.h"

void setUp(void) {
    // This is run before EACH test
}

void tearDown(void) {
    // This is run after EACH test
}

void test_function_add_two_numbers(void) {
    TEST_ASSERT_EQUAL_INT(15, add_two_numbers(10, 5));
    TEST_ASSERT_EQUAL_INT(-3, add_two_numbers(-1, -2));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_function_add_two_numbers);
    return UNITY_END();
}
