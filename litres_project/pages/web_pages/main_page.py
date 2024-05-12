from selene import browser, be, have


class MainPage:
    def open(self):
        browser.open("")
        return self

    def filling_authorization_form(self, user):
        browser.element('[href="/pages/login/"]').should(be.visible).click()
        browser.element('[name="email"]').should(be.visible).type(user.email)
        browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
        browser.element('[name="pwd"]').should(be.visible).type(user.password)
        browser.element('.AuthContent_form__submit__LzXKD > [type="submit"]').should(be.visible).click()
        return self

    def user_must_be_authorized(self, user):
        browser.element('.ProfileButton_profileButton__title__GV_yX').should(be.visible).click()
        browser.open("pages/personal_cabinet_about_me/")
        browser.element('span[class="user_header__name"]').should(have.text(user.name))
        return self

    def user_must_not_be_authorized(self):
        browser.element('.ControlInput_input__error__0DtKl').should(have.text('Неверное сочетание логина и '
                                                                                     'пароля'))
        return self

    def search_book_by_title(self, book):
        # browser.element('[data-testid="search__input"]').should(be.blank).type(book.name)
        browser.element('[data-testid="search__input"]').should(be.blank).type('Война и мир')
        browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    def book_with_specified_title_must_be_found(self):
        # browser.element('[data-testid="art__title"]:nth-child(1)').should(have.text('Семь сестер'))
        browser.element('[data-testid="art__title"]:nth-child(1)').should(have.text('Война и мир'))
        return self

    def search_book_by_author(self, book):
        browser.element('[data-testid="search__input"]').should(be.blank).type(book.author)
        browser.element('[data-testid="search__button"]').should(be.visible).click()
        return self

    def book_with_specified_author_must_be_found(self, book):
        browser.element('[data-testid="art__authorName"]:nth-child(1)').should(have.text(book.author))
        return self


main_page = MainPage()