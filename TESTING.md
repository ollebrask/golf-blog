# Testing

## Manual Testing


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on the Register button | Redirected to the sign up page | Y |          |
| 2           | Click on the sign in link in the form | Redirected to login page | Y |          |
| 5           | Enter valid email | Field will only accept email address format | Y |          |
| 10          | Enter valid password | Field will only accept secure passwords | Y |          |
| 11          | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| 12          | Click on the Sign Up button | Redirected to home page, with succesfully signed in message| Y |          |
| 15          | Click on the Logout butotn | Takes user to sign out page to confirm logout | Y |          |
| 16          | Click "Sign out" button  in the center of the page| Redirects user to home page with you have sign out message | Y |          |
| Log In      |                        |                  |      |             |


---

## Validation:
### HTML Validation:

- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code and pasting it into the validator.

#### add_review.html

![HTML Validation](documentation/validation/add_review.png)

#### delete_comment.html

![HTML Validation](documentation/validation/delete_comment.png)

#### delete_review.html

![HTML Validation](documentation/validation/delete_review.png)

#### edit_comment.html

![HTML Validation](documentation/validation/edit_comment.png)

#### edit_review.html

![HTML Validation](documentation/validation/edit_review.png)

#### index.html

![HTML Validation](documentation/validation/index.png)

#### review_detail.html

![HTML Validation](documentation/validation/review_detail.png)

#### show_golfcourses.html

![HTML Validation](documentation/validation/show_colfcourses.png)

#### add_review.html

![HTML Validation](documentation/validation/show_reviews.png)


### CSS Validation:

- ![CSS Validation](documentation/validation/css-validation.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator.


### Python Validation:

- No errors were found when the code was passed through CI Python Linter[online validation tool](https://pep8ci.herokuapp.com/).  This checking was done manually by copying python code and pasting it into the validator.

#### admin.py

![CI Python Linter. admin.py](documentation/validation/linter-admin.png)

#### forms.py

![CI Python Linter. forms.py](documentation/validation/linter-forms.png)

#### models.py

![CI Python Linter. models.py](documentation/validation/linter-models.png)

#### urls.py

![CI Python Linter. urls.py](documentation/validation/linter-urls.png)

#### views.py

![CI Python Linter. views.py](documentation/validation/linter-views.png)



---
## Lighthouse Report

### Home Page

![Lighthouse Report. Home Page](documentation/lighthouse/lighthouse-home.png)

### Reviews Page

![Lighthouse Report. Reviews Page](documentation/lighthouse/lighthouse-reviews.png)

### Edit review Page

![Lighthouse Report. Edit review Page](documentation/lighthouse/lighthouse-editreview.png)

### Add review Page

![Lighthouse Report. Add review Page](documentation/lighthouse/lighthouse-addreview.png)

### Delete review Page

![Lighthouse Report. Delete review Page](documentation/lighthouse/lighthouse-deletereview.png)

### Detailed review Page

![Lighthouse Report. Detailed review Page](documentation/lighthouse/lighthouse-detailedreview.png)

### Login Page

![Lighthouse Report. Login Page](documentation/lighthouse/lighthouse-login.png)

### Logout Page

![Lighthouse Report. Logout Page](documentation/lighthouse/lighthouse-logout.png)

### Signup Page

![Lighthouse Report. Signup Page](documentation/lighthouse/lighthouse-signup.png)

### Edit comment Page

![Lighthouse Report. Edit comment Page](documentation/lighthouse/lighthouse-editcomment.png)

### Delete comment Page

![Lighthouse Report. Delete comment Page](documentation/lighthouse/lighthouse-deletecomment.png)

### Golfcourses Page

![Lighthouse Report. Golfcourses Page](documentation/lighthouse/lighthouse-golfcourses.png)





---

## Compatibility

Testing was conducted on the following browsers;

- Chrome;
- Safari;


---

# Responsiveness

The responsiveness was checked manually by using devtools in (Chrome) throughout the whole development.


---