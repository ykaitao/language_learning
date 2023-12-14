#include "unity.h"
#include "math_operation.h"

void setUp(void) { /* Do nothing */ }

void tearDown(void) { /* Do nothing */ }

void test_subtract_positive_numbers(void) {
    TEST_ASSERT_EQUAL(5, subtract(10, 5));
}

void test_subtract_negative_numbers(void) {
    TEST_ASSERT_EQUAL(-5, subtract(-10, -5));
}

void test_subtract_zero(void) {
    TEST_ASSERT_EQUAL(10, subtract(10, 0));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_subtract_positive_numbers);
    RUN_TEST(test_subtract_negative_numbers);
    RUN_TEST(test_subtract_zero);
    UNITY_END();

    return 0;
}
