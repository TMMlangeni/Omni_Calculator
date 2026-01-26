import Omni_Calculator as oc
import pytest

# --- Central Tendency Tests ---


def test_calculate_mean():
    assert oc.calculate_mean([10, 20, 30]) == 20.0
    assert oc.calculate_mean([-1, -2, -3]) == -2.0
    # Testing that it raises an error when given a string
    with pytest.raises(TypeError):
        oc.calculate_mean(["dog", "cat"])
    # Testing empty list behavior (assuming ValueError)
    with pytest.raises(ValueError):
        oc.calculate_mean([])


def test_calculate_mode():
    assert oc.calculate_mode([10, 10, 20, 30]) == 10.0
    assert oc.calculate_mode([2.1, 2.1, -3, 8]) == 2.1

    with pytest.raises(ValueError):
        oc.calculate_mode([])


def test_calculate_median():
    # Sorted list
    assert oc.calculate_median([10, 20, 30]) == 20
    # Even number of elements
    assert oc.calculate_median([2, 4, 6, 8]) == 5.0
    # Unsorted list (Crucial test)
    assert oc.calculate_median([2, 1, 5, 7, 3]) == 3
    # Single element
    assert oc.calculate_median([5]) == 5

    # Error checks
    with pytest.raises(ValueError):
        oc.calculate_median([])
    with pytest.raises(TypeError):
        oc.calculate_median(["dog", "cat"])


# --- Spread/Variation Tests ---


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ([10, 20, 30], 10.0),  # Assumes Sample Std Dev (N-1)
        ([5, 5, 5], 0.0),  # Zero variation
        ([1, 2, 3], 1.0),  # Simple increments
        ([1.5, 2.5, 3.5], 1.0),  # Float inputs
        ([-10, -20, -30], 10.0),  # Neg
    ],
)
def test_calculate_std(data_input, expected):
    # Uses approx to handle float precision issues
    assert oc.calculate_std(data_input) == pytest.approx(expected, abs=0.01)

    # Check for empty list
    with pytest.raises(ValueError):
        oc.calculate_std([])


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ([10, 20, 30], 100.0),
        ([5, 5, 5], 0.0),
        ([1, 2, 3], 1.0),
        ([1.5, 2.5, 3.5], 1.0),
        ([-10, -20, -30], 100.0),
    ],
)
def test_calculate_variance(data_input, expected):
    assert oc.calculate_var(data_input) == pytest.approx(expected, abs=0.01)

    # Check for empty list
    with pytest.raises(ValueError):
        oc.calculate_var([])


# --- Probability & Algebra Tests ---


def test_conditional_probability():
    assert round(oc.con_prob(0.5, 0.7), 2) == 0.71
    # Check that it returns None on zero division
    assert oc.con_prob(0.4, 0) is None


def test_quadratic_eq():
    assert oc.quadratic_eq(2, 4, -3) == "x1 = 0.58, x2 = -2.58"
    assert oc.quadratic_eq(2, 4, 2) == "x = -1.00"
    assert oc.quadratic_eq(1, 2, 5) == "There are no real roots"

    # Ensure your main code actually RAISES this error for a=0
    # If it prints a message instead, change this to: assert oc.quadratic_eq(0, 4, 2) == "Your Message"
    with pytest.raises(ZeroDivisionError):
        oc.quadratic_eq(0, 4, 2)
