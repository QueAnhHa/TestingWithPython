# TestingWithPython
Learn how to test applications with Python

## Learn how to structure unit test and integration test.
Notes to myself: 

  First, I need to decide: what I want to test? Am I writing a unit test or an integration test?
  
  Then, I need to structure my test: create inputs (fixtures) , execute the code being tested, capture the output and compare the output with the expected result
  
## Popular Unit test runner in Python: 
 unittest, nose & nose2, pytest

## Testing for Web Framework Django
Django template will create a tests.py file inside your application directory. To execute test suite, use manage.py test

## Integration Test
Testing of multiple components of the application to check that they work together. Integration tests checks more components at once and therefore will have more side effects than a unit test. And integration tetst will require more fixtures to be in place, like a database, a network socket, or a configuration file
