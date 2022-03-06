Feature: Knime Hub API
  Scenario Outline: Create Space
    Examples:
     | spacename                                     | expected_status   |  test_type |
     | test_space_001                                | 201               |  positive  |



  Given request with body and <spacename> which is a <test_type> test
  When put request arrives to endpoint/<spacename>
  Then <expected_status> is responded


  Scenario Outline: Delete Space
    Examples:
     | spacename                                     | expected_status   |  test_type |
     | test_space_001                                | 204               |  positive  |


  Given an existing space with name <spacename> which is a <test_type> test
  When delete request arrives to endpoint
  Then <expected_status> is responded