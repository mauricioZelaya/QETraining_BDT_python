@items
Feature: This will test the Items method feature for the API in todo

  @smoke_test
  Scenario Outline: I want to perform list of the items
    When I send the <SERVICE>
    And I used the <METHOD>
    Then I get the response with <CODE> code

    Examples:
      | SERVICE | METHOD | CODE |
      | items   | GET    | 200  |

  @smoke_test
  Scenario Outline: I want to perform delete of a item
    Given A <SERVICE> and a <METHOD>
    When I select a <ID> of the item
    Then I get the result equals to <CODE>

    Examples:
      | SERVICE | METHOD | ID   | CODE |
      | items   | DELETE | 1033 | 200  |

  @smoke_test
  Scenario Outline: I want to perform Returns the root parent item for the given item Id and
  the Done items. Use RootItem method for unchecked items and DoneRootItem for done items.

    Given that i have the <SERVICE> and the <METHOD>
    When I optained a <ID> with the <ROOT> of Item
    Then I get the status <CODE>

    Examples:
      | SERVICE | METHOD | ID   | ROOT         | CODE |
      | items   | GET    | 1033 | RootItem     | 200  |
      | items   | GET    | 1033 | DoneRootItem | 200  |


  @acceptance_test @crud_test
  Scenario Outline: I want to verify that I delete the items associated to my account
    Given A <SERVICE> and a <METHOD>
    When I select a <ID> of the item
    Then I get the result equals to <CODE>
    And I verify if the <ITEMID> is correctly dislpayed in the response

    Examples:
      | SERVICE | METHOD | ID       | CODE | ITEMID |
      | items   | DELETE | 10049780 | 200  | Id     |
      #| items   | DELETE | 600      | 200  | Id     |
      #| items   | DELETE | 400      | 200  | Id     |

  @crud_test
  Scenario Outline: I want to perform Returns the root parent item for the given item Id and
  the Done items. Use RootItem method for unchecked items and DoneRootItem for done items.

    Given that i have the <SERVICE> and the <METHOD>
    When I optained a <ID> with the <ROOT> of Item
    Then I get the status <CODE>
    And I review if the <ITEMID> is correctly in the response

    Examples:
      | SERVICE | METHOD | ID       | ROOT         | CODE | ITEMID |
      | items   | GET    | 10049805 | RootItem     | 200  | Id     |
      | items   | GET    | 0000     | RootItem     | 200  | Id     |
      | items   | GET    | 789456   | RootItem     | 200  | Id     |
      | items   | GET    | 10049808 | DoneRootItem | 200  | Id     |
      | items   | GET    | 400      | DoneRootItem | 200  | Id     |
      | items   | GET    | 0561     | DoneRootItem | 200  | Id     |