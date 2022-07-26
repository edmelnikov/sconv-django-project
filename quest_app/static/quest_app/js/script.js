// before reading this code, note that I've never programmed on JavaScript
// this code and the idea behind it are both fucking disgusting, but I don't really give a shit since I don't have enough time to make it any cleaner
// good luck figuring it out :)

let global_q_counter = 1; // global question counter
let max_q_number = 16; // maximum number of questions

document.getElementsByClassName("question 1")[0].style.display = 'block'; // show first question
document.getElementById("progress-bar").style.width = 100/max_q_number + "%"; // set initial progress

/* Progress bar */
function move_progress_bar(max_q_num, q_num){
    let step_size = 100 / max_q_num;

    let elem = document.getElementById("progress-bar");
    elem.style.width = q_num*step_size + "%";

}

/* Check if one of the radio buttons with name=q_num is selected */
/* q_num is a question number */
function is_radio_selected(q_num){
    if (document.querySelector('input[name="' + q_num.toString() + '"]:checked') == null) {
        return false;
    }
    else {
        return true;
    }
}

/* Check if the text field with name=q_num is filled */
function is_text_field_filled(q_num){
    let form_value = document.getElementById("answer-age").value;
    if (form_value == "" || !RegExp("^[1-9][0-9]?$|^100$").test(form_value)) {

        return false;
    }
    else {
        return true;
    }
}

/* Show next question or show warning if current question hasn't been answered */
function show_next_q() {
    if (is_radio_selected(global_q_counter) || is_text_field_filled(global_q_counter)) {
        let elements = document.getElementsByClassName("question " + global_q_counter.toString());
        if (elements.length > 0) {
            elements[0].style.display = 'none';  // hide current question
        }
        global_q_counter += 1;
        elements = document.getElementsByClassName("question " + global_q_counter.toString());
        if (elements.length > 0) {
            elements[0].style.display = 'block';  // show next question
            if (global_q_counter >= max_q_number) { // if we've reached the last question
                document.getElementsByClassName("button-next-q")[0].style.display = 'none'; // we hide the "next question" button
                document.getElementsByClassName("button-send")[0].style.display = 'block'; // and we show the "send" button     
            }
        }

        move_progress_bar(max_q_number, global_q_counter);

    }
    else {
        if (global_q_counter == 15) { // this doesn't look good 
            window.alert("Введите возраст");
        }
        else {
            window.alert("Выберите вариант ответа");
        }
    }
}

/* Check if the last question is answered */
function check_last_q() { 
    if (is_radio_selected(global_q_counter)) {
        return true;
    }
    else {
        window.alert("Выберите вариант ответа");
        return false;
    }
}
