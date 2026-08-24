let remaining = 60 * 60;
let timerId = null;

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
}

function renderTimer() {
  const timer = document.getElementById("timer");
  timer.textContent = formatTime(remaining);
  timer.classList.toggle("warning", remaining <= 10 * 60 && remaining > 0);
  timer.classList.toggle("over", remaining === 0);
}

function setState(message) {
  document.getElementById("timerState").textContent = message;
}

function startTimer() {
  if (timerId || remaining === 0) return;
  setState("Running — solutions stay closed until you open them");
  timerId = window.setInterval(() => {
    remaining -= 1;
    renderTimer();
    if (remaining === 0) {
      pauseTimer();
      setState("Time is up. Stop writing and mark what is on the page.");
      document.title = "Time up — DPEN103 mock";
    }
  }, 1000);
}

function pauseTimer() {
  if (!timerId) return;
  window.clearInterval(timerId);
  timerId = null;
  if (remaining > 0) setState("Paused");
}

function resetTimer() {
  pauseTimer();
  remaining = 60 * 60;
  renderTimer();
  setState("Ready for 60 minutes");
}

function gradeAutoQuestions() {
  let correct = 0;
  let answered = 0;
  const questions = document.querySelectorAll(".auto-question");

  questions.forEach((question) => {
    question.classList.remove("correct", "incorrect");
    const selected = question.querySelector("input:checked");
    if (!selected) return;
    answered += 1;
    const isCorrect = selected.value === question.dataset.answer;
    question.classList.add(isCorrect ? "correct" : "incorrect");
    if (isCorrect) correct += 1;
  });

  const score = document.getElementById("score");
  score.innerHTML =
    `${correct}/${questions.length} auto-marked points correct` +
    `<small>${answered}/${questions.length} answered. Mark the written section separately using its marking guides.</small>`;
  score.scrollIntoView({ behavior: "smooth", block: "center" });
}

function revealAll() {
  document.querySelectorAll("details.solution").forEach((item) => {
    item.open = true;
  });
}

function clearExam() {
  if (!window.confirm("Clear every selected answer and written response?")) return;
  document.querySelectorAll("input[type=radio]").forEach((input) => {
    input.checked = false;
  });
  document.querySelectorAll("textarea").forEach((area) => {
    area.value = "";
  });
  document.querySelectorAll(".question").forEach((question) => {
    question.classList.remove("correct", "incorrect");
  });
  document.querySelectorAll("details.solution").forEach((item) => {
    item.open = false;
  });
  document.getElementById("score").innerHTML =
    `Not marked yet<small>Auto-marked section first; written answers use the guides.</small>`;
  resetTimer();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

document.addEventListener("DOMContentLoaded", renderTimer);
