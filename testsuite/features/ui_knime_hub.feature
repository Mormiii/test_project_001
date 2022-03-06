#Feature: Knime Hub UI
#  Scenario Outline: Login
#    Examples:
#     | username                                     | password   |  comment |
#     | Test_Knime_001                               | Jelszo     |  positiv testcase |
#     | Test_Knime_001                               | badpw      |  negativ testcase |
#
#
#  Given user fills <username> and <password> on login page
#  When clicks on login
#  Then if creditentials are correct logged in page is showed

  Scenario: Accessing spaces and UI verification

  Given logged in user with <username> and <password> viewing their spaces
  When page is fully loaded
  Then verifying elements on the page
    Examples:
     | username        | password   |  comment          |         
     | Test_Knime_001  | Jelszo     |  positiv testcase |
#     | Test_Knime_001  | badpw      |  negativ testcase |



  Scenario Outline: Creating a new public space
    Examples:
     | username        | password  | spacename       |
     | Test_Knime_001  | Jelszo    | new_space-00001 |

  Given logged in user with <username> and <password> viewing their spaces
  When user creates a new public space with <spacename>
  Then newly created space is visible under spaces

  Scenario Outline: Deleting a space
    Examples:
     | username        | password | spacename |
     | Test_Knime_001  | Jelszo   | new_space-00001    |

  Given logged in user with <username> and <password> viewing their spaces
  When user deletes the choosen space with <spacename>
  Then the deleted space is no longer visible in spaces