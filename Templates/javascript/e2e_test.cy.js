describe("Verify that some component component exist ", () => {
  beforeEach("navigate to Home page", () => {
    // clear storage and cookies
    cy.clearAllSessionStorage();
    cy.clearLocalStorage();
    cy.clearCookies();

    // load test data
    cy.fixture("test_data.json").then(function (test_data) {
      this.testData = test_data;
    });
  });

  it(
    "checking the components appearance",
    { tags: ["tag1", "tag2"] },
    function () {
      // insert commands here
    }
  );
});
