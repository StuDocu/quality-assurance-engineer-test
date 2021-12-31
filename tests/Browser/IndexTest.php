<?php

namespace Tests\Browser;

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;
use Tests\Browser\Components\QuestionMaker;
use Tests\Browser\Components\Questions;
use Tests\Browser\Pages\IndexPage;
use Tests\DuskTestCase;

class IndexTest extends DuskTestCase
{
    /**
     * Test display and hide instruction when toggling question.
     *
     * @return void
     */
    public function testDisplayAndHideAnswerWhenTogglingQuestion()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit(new IndexPage)
                ->within(new Questions, function ($browser) {
                    $browser->assertSeeIn("li:nth-of-type(1) > .question__question", "How to add a question?")
                        ->assertDontSeeIn("li:nth-of-type(1) > .question__answer", "Just use the form below!")
                        ->click("li:nth-of-type(1) > .question__question")
                        ->assertSeeIn("li:nth-of-type(1) > .question__answer", "Just use the form below!")
                        ->click(".question__question")
                        ->assertDontSeeIn("li:nth-of-type(1) > .question__answer", "Just use the form below!");
                });
        });
    }

    /**
     * Test add question.
     *
     * @return void
     */
    public function testAddQuestion()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit(new IndexPage)
                ->assertSeeIn(".sidebar", "1 question");
            $this->addQuestion($browser, "2nd Question", "2nd Answer");
            $browser->within(new Questions, function ($browser) {
                    $browser->waitFor("li:nth-of-type(2) > .question__question")
                        ->assertSeeIn("li:nth-of-type(2) > .question__question", "2nd Question")
                        ->click("li:nth-of-type(2) > .question__question")
                        ->assertSeeIn("li:nth-of-type(2) > .question__answer", "2nd Answer");
                })
                ->assertDontSeeIn(".sidebar", "1 question")
                ->assertSeeIn(".sidebar", "2 questions");
        });
    }

    /**
     * Test sort questions.
     *
     * @return void
     */
    public function testSortQuestions()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit(new IndexPage)
                ->within(new Questions, function ($browser) {
                    $browser->assertSeeIn("li:nth-of-type(1) > .question__question", "How to add a question?");
                })
                ->assertSeeIn(".sidebar", "1 question");

            // Add 2nd question
            $this->addQuestion($browser, "2nd Question", "2nd Answer");
            $browser->within(new Questions, function ($browser) {
                $browser->assertSeeIn("li:nth-of-type(2) > .question__question", "2nd Question");
            });
            $browser->assertSeeIn(".sidebar", "2 questions");

            // Add 3rd question
            $this->addQuestion($browser, "3rd Question", "3rd Answer");
            $browser->within(new Questions, function ($browser) {
                $browser->assertSeeIn("li:nth-of-type(3) > .question__question", "3rd Question");
            });
            $browser->assertSeeIn(".sidebar", "3 questions");

            // Sort questions
            $browser->within(new Questions, function ($browser) {
                $browser->press("Sort questions")
                    ->assertSeeIn("li:nth-of-type(1) > .question__question", "2nd Question")
                    ->assertSeeIn("li:nth-of-type(2) > .question__question", "3rd Question")
                    ->assertSeeIn("li:nth-of-type(3) > .question__question", "How to add a question?")
                    ->click("li:nth-of-type(1) > .question__question")
                    ->assertSeeIn("li:nth-of-type(1) > .question__answer", "2nd Answer")
                    ->click("li:nth-of-type(2) > .question__question")
                    ->assertSeeIn("li:nth-of-type(2) > .question__answer", "3rd Answer")
                    ->click("li:nth-of-type(3) > .question__question")
                    ->assertSeeIn("li:nth-of-type(3) > .question__answer", "Just use the form below!");
                });
        });
    }

    /**
     * Test remove questions.
     *
     * @return void
     */
    public function testRemoveQuestions()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit(new IndexPage)
                ->within(new Questions, function ($browser) {
                    $browser->assertSeeIn("li:nth-of-type(1) > .question__question", "How to add a question?");
                })
                ->assertSeeIn(".sidebar", "1 question");

            // Add 2nd question
            $this->addQuestion($browser, "2nd Question", "2nd Answer");
            $browser->within(new Questions, function ($browser) {
                $browser->assertSeeIn("li:nth-of-type(2) > .question__question", "2nd Question");
                })
                ->assertSeeIn(".sidebar", "2 questions");

            // Add 3rd question
            $this->addQuestion($browser, "3rd Question", "3rd Answer");
            $browser->within(new Questions, function ($browser) {
                $browser->assertSeeIn("li:nth-of-type(3) > .question__question", "3rd Question");
                })
                ->assertSeeIn(".sidebar", "3 questions");

            // Remove questions
            $browser->within(new Questions, function ($browser)
            {
                $browser->press("Remove questions")
                    ->waitFor(".alert-danger")
                    ->assertSeeIn(".alert-danger", "No questions yet :-(")
                    ->assertMissing("li:nth-of-type(1) > .question__question")
                    ->assertMissing("li:nth-of-type(2) > .question__question")
                    ->assertMissing("li:nth-of-type(3) > .question__question")
                    ->assertDontSee("How to add a question?")
                    ->assertDontSee("2nd Question")
                    ->assertDontSee("3rd Question");
                })
                ->assertSeeIn(".sidebar", "no questions");
        });
    }

    /**
     * Test add first question.
     *
     * @return void
     */
    public function testAddFirstQuestion()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit(new IndexPage)
                    ->press("Remove questions")
                    ->waitFor(".alert-danger")
                    ->assertSeeIn(".alert-danger", "No questions yet :-(")
                    ->assertSeeIn(".sidebar", "no questions");
            $this->addQuestion($browser, "1st Question", "1st Answer");
            $browser->within(new Questions, function ($browser) {
                $browser->waitFor("li:nth-of-type(1) > .question__question")
                    ->assertSeeIn("li:nth-of-type(1) > .question__question", "1st Question")
                    ->click("li:nth-of-type(1) > .question__question")
                    ->assertSeeIn("li:nth-of-type(1) > .question__answer", "1st Answer");
                })
                ->assertMissing(".alert-danger")
                ->assertDontSee("No questions yet :-(")
                ->assertSeeIn(".sidebar", "1 question");
        });
    }

    /**
     * Test question and answer fields are required.
     *
     * @return void
     */
    public function testQuestionAndAnswerFieldsAreRequired()
    {
        $this->browse(function (Browser $browser) {
            $browser->visit(new IndexPage);
            $this->addQuestion($browser, "Question", "");
            $browser->assertMissing("li:nth-of-type(2) > .question__question");

            $browser->visit(new IndexPage);
            $this->addQuestion($browser, "", "Answer");
            $browser->assertMissing("li:nth-of-type(2) > .question__question");
        });
    }

    private function addQuestion($browser, $question, $answer)
    {
        $browser->within(new QuestionMaker, function ($browser) use ($question, $answer) {
            $browser->type("#question", $question)
                ->type("#answer", $answer)
                ->click(".btn-success");
            });
    }
}
