Feature: TestGenerator Functionality

  Scenario: Generating All Combinations of Choices (ACoC)
    Given the following characteristics
      | characteristic | values     |
      | a              | a1, a2     |
      | b              | b1, b2, b3 |
      | c              | c1, c2     |
    When I generate ACoC test cases
    Then the result should be
      | result     |
      | a1, b1, c1 |
      | a1, b1, c2 |
      | a1, b2, c1 |
      | a1, b2, c2 |
      | a1, b3, c1 |
      | a1, b3, c2 |
      | a2, b1, c1 |
      | a2, b1, c2 |
      | a2, b2, c1 |
      | a2, b2, c2 |
      | a2, b3, c1 |
      | a2, b3, c2 |

  Scenario: Generating Each Choice Combinations (ECC)
    Given the following characteristics
      | characteristic | values     |
      | a              | a1, a2     |
      | b              | b1, b2, b3 |
      | c              | c1, c2     |
    When I generate ECC test cases
    Then the result should be
      | result     |
      | a1, b1, c1 |
      | a2, b2, c2 |
      | a1, b3, c1 |

  Scenario: Generating Base Choice Combinations (BCC)
    Given the following characteristics
      | characteristic | values     |
      | a              | a1, a2     |
      | b              | b1, b2, b3 |
      | c              | c1, c2     |
    And the base choice is
      | characteristic | value |
      | a              | a1    |
      | b              | b1    |
      | c              | c1    |
    When I generate BCC test cases
    Then the result should be
      | result     |
      | a1, b1, c1 |
      | a2, b1, c1 |
      | a1, b2, c1 |
      | a1, b3, c1 |
      | a1, b1, c2 |

  Scenario: Generating Multiple Base Choice Combinations (MBCC)
    Given the following characteristics
      | characteristic | values     |
      | a              | a1, a2     |
      | b              | b1, b2, b3 |
      | c              | c1, c2     |
    And the base tests are
      | base_tests |
      | a1, b1, c1 |
      | a2, b2, c2 |
    When I generate MBCC test cases
    Then the result should be
      | result     |
      | a1, b1, c1 |
      | a2, b2, c2 |
      | a2, b1, c1 |
      | a1, b2, c1 |
      | a1, b1, c2 |
      | a1, b3, c1 |
      | a1, b2, c2 |
      | a2, b1, c2 |
      | a2, b3, c2 |
      | a2, b2, c1 |
