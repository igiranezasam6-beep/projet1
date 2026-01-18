const STORAGE_KEYS = {
  exercises: "eduburundi_exercises",
  forum: "eduburundi_forum",
  chat: "eduburundi_chat",
  language: "eduburundi_language",
};

const seedExercises = [
  {
    id: "math-01",
    subject: "Mathematiques",
    level: "College",
    theme: "Algebre",
    title: "Equations du premier degre",
    statement: "Resoudre 3x + 7 = 25 puis verifier la solution.",
    solution: "3x = 18 donc x = 6. Verification: 3*6 + 7 = 25.",
    video: "https://www.youtube.com/watch?v=1O6b0w_2g2Q",
    teacher: "Mme Aline",
    questions: [],
  },
  {
    id: "phy-01",
    subject: "Physique",
    level: "Lycee",
    theme: "Electricite",
    title: "Loi d'Ohm",
    statement:
      "Un circuit a une tension de 12 V et un courant de 0,4 A. Calculer la resistance.",
    solution: "R = U / I = 12 / 0,4 = 30 ohms.",
    video: "https://www.youtube.com/watch?v=Vh8IAbhC0VU",
    teacher: "M. David",
    questions: [],
  },
  {
    id: "fra-01",
    subject: "Francais",
    level: "College",
    theme: "Grammaire",
    title: "Accord du participe passe",
    statement:
      "Expliquez la regle d'accord du participe passe avec l'auxiliaire etre.",
    solution:
      "Avec etre, le participe passe s'accorde en genre et en nombre avec le sujet.",
    video: "",
    teacher: "Mme Chantal",
    questions: [],
  },
];

const seedForumThreads = [
  {
    id: "thread-01",
    subject: "Mathematiques",
    level: "College",
    author: "Jean",
    message: "Comment memoriser les identites remarquables ?",
    createdAt: new Date().toISOString(),
    replies: [
      {
        id: "reply-01",
        author: "Grace",
        message: "Fais des fiches et pratique 5 exercices par semaine.",
        createdAt: new Date().toISOString(),
      },
    ],
  },
];

const i18n = {
  fr: {
    brandName: "EduBurundi",
    brandTagline: "Plateforme d'exercices interactifs",
    navTeacher: "Espace enseignants",
    navStudent: "Espace eleves",
    navChatbot: "Chatbot",
    navForum: "Forum",
    langLabel: "Langue",
    heroTitle: "Apprendre, reviser et progresser partout au Burundi",
    heroSubtitle:
      "EduBurundi rassemble exercices, corriges, videos et entraide pour les eleves du post-fondamental.",
    heroCta: "Explorer les exercices",
    heroCtaAlt: "Publier un exercice",
    heroCardTitle: "En bref",
    heroCardPoint1: "Contenus par matiere et niveau",
    heroCardPoint2: "Questions et discussions faciles",
    heroCardPoint3: "Chatbot d'assistance integre",
    heroCardPoint4: "Multilingue FR/EN/RN",
    featureTeacherTitle: "Espace enseignants",
    featureTeacherDesc:
      "Publiez des exercices classes par matiere, niveau et theme, avec corriges et liens video.",
    featureStudentTitle: "Espace eleves",
    featureStudentDesc:
      "Trouvez rapidement les ressources utiles pour reviser et poser des questions.",
    featureChatbotTitle: "Chatbot d'assistance",
    featureChatbotDesc:
      "Obtenez de l'aide pour naviguer, comprendre et acceder aux contenus.",
    featureForumTitle: "Forum d'entraide",
    featureForumDesc:
      "Discutez par matiere ou niveau avec moderation legere.",
    teacherTitle: "Espace enseignants",
    teacherSubtitle:
      "Televersez des exercices, ajoutez des corriges et suivez l'interet.",
    teacherNameLabel: "Nom de l'enseignant",
    teacherNamePlaceholder: "Ex: Mme Aline",
    teacherSubjectLabel: "Matiere",
    teacherSubjectPlaceholder: "Ex: Mathematiques",
    teacherLevelLabel: "Niveau",
    teacherLevelPlaceholder: "Ex: College",
    teacherThemeLabel: "Theme",
    teacherThemePlaceholder: "Ex: Algebre",
    teacherTitleLabel: "Titre de l'exercice",
    teacherTitlePlaceholder: "Ex: Equations du premier degre",
    teacherStatementLabel: "Enonce",
    teacherStatementPlaceholder: "Detaillez l'exercice a proposer.",
    teacherSolutionLabel: "Corrige (optionnel)",
    teacherSolutionPlaceholder: "Indiquez la solution ou les etapes.",
    teacherVideoLabel: "Lien video (optionnel)",
    teacherVideoPlaceholder: "https://www.youtube.com/...",
    teacherSubmit: "Publier l'exercice",
    teacherPublishedTitle: "Exercices publies",
    teacherSuccess: "Exercice publie avec succes.",
    studentTitle: "Espace eleves",
    studentSubtitle:
      "Recherchez des ressources par matiere, niveau ou theme et posez vos questions.",
    filterSubjectLabel: "Matiere",
    filterLevelLabel: "Niveau",
    filterThemeLabel: "Theme",
    filterSearchLabel: "Recherche",
    filterSearchPlaceholder: "Mot cle, titre, sujet...",
    filterAllSubjects: "Toutes les matieres",
    filterAllLevels: "Tous les niveaux",
    filterAllThemes: "Tous les themes",
    exerciseNoResults: "Aucun exercice ne correspond aux filtres.",
    exerciseQuestionsTitle: "Questions des eleves",
    exerciseQuestionNamePlaceholder: "Votre nom",
    exerciseQuestionTextPlaceholder: "Posez votre question...",
    exerciseQuestionSubmit: "Envoyer",
    exerciseViewSolution: "Voir corrige",
    exerciseHideSolution: "Masquer corrige",
    exerciseDownload: "Telecharger",
    exerciseVideo: "Voir video",
    chatbotTitle: "Chatbot d'assistance",
    chatbotSubtitle:
      "Posez vos questions pratiques et recevez des conseils adaptes a votre niveau.",
    chatbotPlaceholder: "Tapez votre question...",
    chatbotSend: "Envoyer",
    chatbotWelcome:
      "Bonjour ! Je peux aider a trouver des exercices, videos ou forums.",
    chatbotSuggestion:
      "Essayez: 'Je cherche des exercices de maths' ou 'Ou trouver les corriges ?'",
    forumTitle: "Forum d'entraide",
    forumSubtitle:
      "Lancez des discussions par matiere ou niveau, avec moderation legere.",
    forumNameLabel: "Nom ou pseudo",
    forumNamePlaceholder: "Ex: Amina",
    forumSubjectLabel: "Matiere",
    forumSubjectPlaceholder: "Ex: Physique",
    forumLevelLabel: "Niveau",
    forumLevelPlaceholder: "Ex: Lycee",
    forumMessageLabel: "Message d'ouverture",
    forumMessagePlaceholder: "Decrivez votre question ou sujet.",
    forumSubmit: "Ouvrir la discussion",
    forumReplyPlaceholder: "Votre reponse...",
    forumReplyButton: "Repondre",
    footerText:
      "EduBurundi - Soutenir les revisions et l'acces aux ressources educatives pour tous.",
  },
  en: {
    brandName: "EduBurundi",
    brandTagline: "Interactive exercises platform",
    navTeacher: "Teacher space",
    navStudent: "Student space",
    navChatbot: "Chatbot",
    navForum: "Forum",
    langLabel: "Language",
    heroTitle: "Learn, revise, and progress across Burundi",
    heroSubtitle:
      "EduBurundi brings exercises, solutions, videos, and peer support for post-basic students.",
    heroCta: "Explore exercises",
    heroCtaAlt: "Publish an exercise",
    heroCardTitle: "At a glance",
    heroCardPoint1: "Content by subject and level",
    heroCardPoint2: "Easy questions and discussions",
    heroCardPoint3: "Built-in assistance chatbot",
    heroCardPoint4: "Multilingual FR/EN/RN",
    featureTeacherTitle: "Teacher space",
    featureTeacherDesc:
      "Publish exercises by subject, level, and theme with solutions and video links.",
    featureStudentTitle: "Student space",
    featureStudentDesc:
      "Quickly find resources for revision and ask questions.",
    featureChatbotTitle: "Assistance chatbot",
    featureChatbotDesc:
      "Get help navigating the site and accessing the right content.",
    featureForumTitle: "Peer forum",
    featureForumDesc: "Discuss by subject or level with light moderation.",
    teacherTitle: "Teacher space",
    teacherSubtitle:
      "Upload exercises, add solutions, and track engagement.",
    teacherNameLabel: "Teacher name",
    teacherNamePlaceholder: "Ex: Ms. Aline",
    teacherSubjectLabel: "Subject",
    teacherSubjectPlaceholder: "Ex: Mathematics",
    teacherLevelLabel: "Level",
    teacherLevelPlaceholder: "Ex: Lower secondary",
    teacherThemeLabel: "Theme",
    teacherThemePlaceholder: "Ex: Algebra",
    teacherTitleLabel: "Exercise title",
    teacherTitlePlaceholder: "Ex: First degree equations",
    teacherStatementLabel: "Statement",
    teacherStatementPlaceholder: "Describe the exercise.",
    teacherSolutionLabel: "Solution (optional)",
    teacherSolutionPlaceholder: "Provide solution steps.",
    teacherVideoLabel: "Video link (optional)",
    teacherVideoPlaceholder: "https://www.youtube.com/...",
    teacherSubmit: "Publish exercise",
    teacherPublishedTitle: "Published exercises",
    teacherSuccess: "Exercise published successfully.",
    studentTitle: "Student space",
    studentSubtitle:
      "Search by subject, level, or theme and ask your questions.",
    filterSubjectLabel: "Subject",
    filterLevelLabel: "Level",
    filterThemeLabel: "Theme",
    filterSearchLabel: "Search",
    filterSearchPlaceholder: "Keyword, title, topic...",
    filterAllSubjects: "All subjects",
    filterAllLevels: "All levels",
    filterAllThemes: "All themes",
    exerciseNoResults: "No exercises match the selected filters.",
    exerciseQuestionsTitle: "Student questions",
    exerciseQuestionNamePlaceholder: "Your name",
    exerciseQuestionTextPlaceholder: "Ask your question...",
    exerciseQuestionSubmit: "Send",
    exerciseViewSolution: "View solution",
    exerciseHideSolution: "Hide solution",
    exerciseDownload: "Download",
    exerciseVideo: "Watch video",
    chatbotTitle: "Assistance chatbot",
    chatbotSubtitle:
      "Ask practical questions and get guidance for your level.",
    chatbotPlaceholder: "Type your question...",
    chatbotSend: "Send",
    chatbotWelcome:
      "Hello! I can help you find exercises, videos, or forums.",
    chatbotSuggestion:
      "Try: 'I need math exercises' or 'Where are the solutions?'",
    forumTitle: "Peer forum",
    forumSubtitle:
      "Start discussions by subject or level with light moderation.",
    forumNameLabel: "Name or nickname",
    forumNamePlaceholder: "Ex: Amina",
    forumSubjectLabel: "Subject",
    forumSubjectPlaceholder: "Ex: Physics",
    forumLevelLabel: "Level",
    forumLevelPlaceholder: "Ex: Upper secondary",
    forumMessageLabel: "Opening message",
    forumMessagePlaceholder: "Describe your question or topic.",
    forumSubmit: "Open discussion",
    forumReplyPlaceholder: "Your reply...",
    forumReplyButton: "Reply",
    footerText:
      "EduBurundi - Supporting revision and access to learning resources for all.",
  },
  rn: {
    brandName: "EduBurundi",
    brandTagline: "Ihuriro ry'imyimenyerezo",
    navTeacher: "Abarimu",
    navStudent: "Abanyeshure",
    navChatbot: "Chatbot",
    navForum: "Forum",
    langLabel: "Ururimi",
    heroTitle: "Twigire hamwe mu Burundi hose",
    heroSubtitle:
      "EduBurundi ikoranya imyimenyerezo, ibisubizo, amavidewo n'imfashanyo ku banyeshure.",
    heroCta: "Raba imyimenyerezo",
    heroCtaAlt: "Shira ikibazo",
    heroCardTitle: "Mu ncamake",
    heroCardPoint1: "Ibikoresho ukurikije ivyigwa n'igice",
    heroCardPoint2: "Ibibazo n'ibiganiro vyoroshe",
    heroCardPoint3: "Chatbot yo gufasha",
    heroCardPoint4: "FR/EN/RN",
    featureTeacherTitle: "Abarimu",
    featureTeacherDesc:
      "Shira imyimenyerezo ukurikije ivyigwa, igice n'umurongo, hamwe n'ibisubizo.",
    featureStudentTitle: "Abanyeshure",
    featureStudentDesc:
      "Rondera ibikoresho vyo gusubiramwo no kubaza ibibazo.",
    featureChatbotTitle: "Chatbot yo gufasha",
    featureChatbotDesc: "Fasha mu kuyobora no kuronka ibikenewe.",
    featureForumTitle: "Forum y'ubufasha",
    featureForumDesc: "Biganiro ku vyigwa canke ku rwego.",
    teacherTitle: "Abarimu",
    teacherSubtitle:
      "Shira imyimenyerezo, ongerako ibisubizo, kandi ukurikirane.",
    teacherNameLabel: "Izina ry'umwigisha",
    teacherNamePlaceholder: "Nk'akarorero: Mme Aline",
    teacherSubjectLabel: "Icigwa",
    teacherSubjectPlaceholder: "Nk'akarorero: Mathematiques",
    teacherLevelLabel: "Urwego",
    teacherLevelPlaceholder: "Nk'akarorero: College",
    teacherThemeLabel: "Insiguro",
    teacherThemePlaceholder: "Nk'akarorero: Algebre",
    teacherTitleLabel: "Umutwe w'imyimenyerezo",
    teacherTitlePlaceholder: "Nk'akarorero: Equations",
    teacherStatementLabel: "Ivyo gukora",
    teacherStatementPlaceholder: "Sobanura ikibazo.",
    teacherSolutionLabel: "Ibisubizo (bidakenewe)",
    teacherSolutionPlaceholder: "Shiramwo ibisubizo.",
    teacherVideoLabel: "Lien video (bidakenewe)",
    teacherVideoPlaceholder: "https://www.youtube.com/...",
    teacherSubmit: "Shira imyimenyerezo",
    teacherPublishedTitle: "Imyimenyerezo yashizwe",
    teacherSuccess: "Imyimenyerezo yashizwe neza.",
    studentTitle: "Abanyeshure",
    studentSubtitle:
      "Rondera ibikoresho ukurikije icigwa, urwego canke insiguro.",
    filterSubjectLabel: "Icigwa",
    filterLevelLabel: "Urwego",
    filterThemeLabel: "Insiguro",
    filterSearchLabel: "Rondera",
    filterSearchPlaceholder: "Ijambo ry'ingenzi...",
    filterAllSubjects: "Ivyigwa vyose",
    filterAllLevels: "Inzego zose",
    filterAllThemes: "Insiguro zose",
    exerciseNoResults: "Nta myimenyerezo ihuye n'ivyo murondera.",
    exerciseQuestionsTitle: "Ibibazo vy'abanyeshure",
    exerciseQuestionNamePlaceholder: "Izina ryawe",
    exerciseQuestionTextPlaceholder: "Shira ikibazo cawe...",
    exerciseQuestionSubmit: "Ohereza",
    exerciseViewSolution: "Raba ibisubizo",
    exerciseHideSolution: "Hisha ibisubizo",
    exerciseDownload: "Kuramwo",
    exerciseVideo: "Raba video",
    chatbotTitle: "Chatbot yo gufasha",
    chatbotSubtitle:
      "Baza ibibazo ku buryo bwo gukoresha no kuronka ibikoresho.",
    chatbotPlaceholder: "Andika ikibazo cawe...",
    chatbotSend: "Ohereza",
    chatbotWelcome:
      "Muraho! Ndagufasha kuronka imyimenyerezo, amavidewo canke forum.",
    chatbotSuggestion:
      "Gerageza: 'Ndondera imyimenyerezo ya maths' canke 'Noba ndeye ibisubizo?'",
    forumTitle: "Forum y'ubufasha",
    forumSubtitle:
      "Tanguza ibiganiro ukurikije icigwa canke urwego.",
    forumNameLabel: "Izina canke izina ry'igiturire",
    forumNamePlaceholder: "Nk'akarorero: Amina",
    forumSubjectLabel: "Icigwa",
    forumSubjectPlaceholder: "Nk'akarorero: Physique",
    forumLevelLabel: "Urwego",
    forumLevelPlaceholder: "Nk'akarorero: Lycee",
    forumMessageLabel: "Ubutumwa bwo gutangura",
    forumMessagePlaceholder: "Sobanura ikibazo canke insiguro.",
    forumSubmit: "Tanguza ikiganiro",
    forumReplyPlaceholder: "Inyishu yawe...",
    forumReplyButton: "Subiza",
    footerText:
      "EduBurundi - Gufasha gusubiramwo no gushikira ibikoresho vy'inyigisho kuri bose.",
  },
};

const state = {
  exercises: loadFromStorage(STORAGE_KEYS.exercises, seedExercises),
  forumThreads: loadFromStorage(STORAGE_KEYS.forum, seedForumThreads),
  chatHistory: loadFromStorage(STORAGE_KEYS.chat, []),
  language: loadFromStorage(STORAGE_KEYS.language, "fr"),
};

const dom = {};

document.addEventListener("DOMContentLoaded", () => {
  cacheDom();
  bindEvents();
  ensureChatWelcome();
  applyTranslations();
  renderAll();
});

function cacheDom() {
  dom.languageSelect = document.getElementById("languageSelect");
  dom.teacherForm = document.getElementById("teacherForm");
  dom.teacherStatus = document.getElementById("teacherStatus");
  dom.teacherExercises = document.getElementById("teacherExercises");
  dom.filterSubject = document.getElementById("filterSubject");
  dom.filterLevel = document.getElementById("filterLevel");
  dom.filterTheme = document.getElementById("filterTheme");
  dom.filterSearch = document.getElementById("filterSearch");
  dom.exerciseList = document.getElementById("exerciseList");
  dom.chatbotMessages = document.getElementById("chatbotMessages");
  dom.chatbotForm = document.getElementById("chatbotForm");
  dom.chatbotInput = document.getElementById("chatbotInput");
  dom.forumForm = document.getElementById("forumForm");
  dom.forumThreads = document.getElementById("forumThreads");

  if (dom.languageSelect) {
    dom.languageSelect.value = state.language;
  }
}

function bindEvents() {
  dom.languageSelect?.addEventListener("change", (event) => {
    state.language = event.target.value;
    saveToStorage(STORAGE_KEYS.language, state.language);
    applyTranslations();
    renderAll();
  });

  dom.teacherForm?.addEventListener("submit", handleTeacherSubmit);

  [dom.filterSubject, dom.filterLevel, dom.filterTheme].forEach((select) => {
    select?.addEventListener("change", renderExercises);
  });

  dom.filterSearch?.addEventListener("input", renderExercises);

  dom.exerciseList?.addEventListener("click", handleExerciseClick);
  dom.exerciseList?.addEventListener("submit", handleQuestionSubmit);

  dom.chatbotForm?.addEventListener("submit", handleChatbotSubmit);

  dom.forumForm?.addEventListener("submit", handleForumSubmit);
  dom.forumThreads?.addEventListener("submit", handleForumReplySubmit);
}

function loadFromStorage(key, fallback) {
  try {
    const raw = window.localStorage.getItem(key);
    if (!raw) return structuredClone(fallback);
    return JSON.parse(raw);
  } catch (error) {
    return structuredClone(fallback);
  }
}

function saveToStorage(key, value) {
  try {
    window.localStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    console.warn("LocalStorage not available", error);
  }
}

function t(key) {
  return i18n[state.language]?.[key] || i18n.fr[key] || key;
}

function applyTranslations() {
  document.documentElement.lang = state.language;
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const key = element.dataset.i18n;
    element.textContent = t(key);
  });

  document.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
    const key = element.dataset.i18nPlaceholder;
    element.setAttribute("placeholder", t(key));
  });
}

function renderAll() {
  buildFilterOptions();
  renderTeacherExercises();
  renderExercises();
  renderChatbot();
  renderForumThreads();
}

function buildFilterOptions() {
  const subjects = uniqueValues(state.exercises.map((item) => item.subject));
  const levels = uniqueValues(state.exercises.map((item) => item.level));
  const themes = uniqueValues(state.exercises.map((item) => item.theme));

  buildSelect(dom.filterSubject, subjects, "filterAllSubjects");
  buildSelect(dom.filterLevel, levels, "filterAllLevels");
  buildSelect(dom.filterTheme, themes, "filterAllThemes");
}

function buildSelect(select, values, allLabelKey) {
  if (!select) return;
  const current = select.value || "all";
  select.innerHTML = "";

  const allOption = document.createElement("option");
  allOption.value = "all";
  allOption.textContent = t(allLabelKey);
  select.appendChild(allOption);

  values.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.appendChild(option);
  });

  select.value = values.includes(current) ? current : "all";
}

function renderTeacherExercises() {
  if (!dom.teacherExercises) return;
  dom.teacherExercises.innerHTML = "";

  state.exercises
    .slice()
    .reverse()
    .forEach((exercise) => {
      const item = document.createElement("div");
      item.className = "exercise-card";

      const title = document.createElement("h4");
      title.textContent = exercise.title;

      const meta = document.createElement("div");
      meta.className = "exercise-meta";
      meta.textContent = `${exercise.subject} - ${exercise.level} - ${exercise.theme}`;

      const teacher = document.createElement("div");
      teacher.className = "exercise-meta";
      teacher.textContent = `${exercise.teacher || "Prof"} `;

      item.appendChild(title);
      item.appendChild(meta);
      item.appendChild(teacher);
      dom.teacherExercises.appendChild(item);
    });
}

function renderExercises() {
  if (!dom.exerciseList) return;
  dom.exerciseList.innerHTML = "";

  const filters = getFilters();
  const filtered = state.exercises.filter((exercise) => {
    const matchesSubject =
      filters.subject === "all" || exercise.subject === filters.subject;
    const matchesLevel =
      filters.level === "all" || exercise.level === filters.level;
    const matchesTheme =
      filters.theme === "all" || exercise.theme === filters.theme;
    const matchesSearch =
      !filters.search ||
      [exercise.title, exercise.statement, exercise.theme]
        .join(" ")
        .toLowerCase()
        .includes(filters.search);
    return matchesSubject && matchesLevel && matchesTheme && matchesSearch;
  });

  if (filtered.length === 0) {
    const empty = document.createElement("div");
    empty.className = "exercise-card";
    empty.textContent = t("exerciseNoResults");
    dom.exerciseList.appendChild(empty);
    return;
  }

  filtered.forEach((exercise) => {
    const card = document.createElement("article");
    card.className = "exercise-card";

    const title = document.createElement("h3");
    title.textContent = exercise.title;

    const meta = document.createElement("div");
    meta.className = "exercise-meta";
    meta.textContent = `${exercise.subject} - ${exercise.level} - ${exercise.theme}`;

    const statement = document.createElement("p");
    statement.className = "exercise-statement";
    statement.textContent = exercise.statement;

    const solution = document.createElement("p");
    solution.className = "exercise-statement is-hidden exercise-solution";
    solution.textContent =
      exercise.solution || t("teacherSolutionPlaceholder");

    const actions = document.createElement("div");
    actions.className = "exercise-actions";

    const toggleButton = document.createElement("button");
    toggleButton.className = "secondary-btn";
    toggleButton.type = "button";
    toggleButton.dataset.action = "toggle-solution";
    toggleButton.dataset.exerciseId = exercise.id;
    toggleButton.textContent = t("exerciseViewSolution");

    const downloadButton = document.createElement("button");
    downloadButton.className = "secondary-btn";
    downloadButton.type = "button";
    downloadButton.dataset.action = "download";
    downloadButton.dataset.exerciseId = exercise.id;
    downloadButton.textContent = t("exerciseDownload");

    actions.appendChild(toggleButton);
    actions.appendChild(downloadButton);

    if (exercise.video) {
      const videoLink = document.createElement("a");
      videoLink.className = "secondary-btn";
      videoLink.href = exercise.video;
      videoLink.target = "_blank";
      videoLink.rel = "noopener noreferrer";
      videoLink.textContent = t("exerciseVideo");
      actions.appendChild(videoLink);
    }

    const questionsTitle = document.createElement("h4");
    questionsTitle.textContent = t("exerciseQuestionsTitle");

    const questionsList = document.createElement("div");
    questionsList.className = "forum-replies";

    exercise.questions.forEach((question) => {
      const item = document.createElement("div");
      item.className = "forum-reply";
      item.textContent = question.message;
      const metaText = document.createElement("span");
      metaText.textContent = `${question.author} - ${formatDate(
        question.createdAt
      )}`;
      item.appendChild(metaText);
      questionsList.appendChild(item);
    });

    const questionForm = document.createElement("form");
    questionForm.className = "forum-reply-form";
    questionForm.dataset.exerciseId = exercise.id;

    const nameInput = document.createElement("input");
    nameInput.name = "author";
    nameInput.type = "text";
    nameInput.placeholder = t("exerciseQuestionNamePlaceholder");
    nameInput.required = true;

    const questionInput = document.createElement("input");
    questionInput.name = "message";
    questionInput.type = "text";
    questionInput.placeholder = t("exerciseQuestionTextPlaceholder");
    questionInput.required = true;

    const submitButton = document.createElement("button");
    submitButton.className = "secondary-btn";
    submitButton.type = "submit";
    submitButton.textContent = t("exerciseQuestionSubmit");

    questionForm.appendChild(nameInput);
    questionForm.appendChild(questionInput);
    questionForm.appendChild(submitButton);

    card.appendChild(title);
    card.appendChild(meta);
    card.appendChild(statement);
    card.appendChild(solution);
    card.appendChild(actions);
    card.appendChild(questionsTitle);
    card.appendChild(questionsList);
    card.appendChild(questionForm);
    dom.exerciseList.appendChild(card);
  });
}

function renderChatbot() {
  if (!dom.chatbotMessages) return;
  dom.chatbotMessages.innerHTML = "";

  state.chatHistory.forEach((message) => {
    const bubble = document.createElement("div");
    bubble.className = `chatbot-bubble ${message.from}`;
    bubble.textContent = message.text;
    dom.chatbotMessages.appendChild(bubble);
  });

  dom.chatbotMessages.scrollTop = dom.chatbotMessages.scrollHeight;
}

function renderForumThreads() {
  if (!dom.forumThreads) return;
  dom.forumThreads.innerHTML = "";

  state.forumThreads
    .slice()
    .reverse()
    .forEach((thread) => {
      const card = document.createElement("div");
      card.className = "forum-thread";

      const title = document.createElement("h4");
      title.textContent = `${thread.subject} - ${thread.level}`;

      const meta = document.createElement("p");
      meta.textContent = `${thread.author} - ${formatDate(thread.createdAt)}`;

      const message = document.createElement("p");
      message.textContent = thread.message;

      const replies = document.createElement("div");
      replies.className = "forum-replies";
      thread.replies.forEach((reply) => {
        const replyItem = document.createElement("div");
        replyItem.className = "forum-reply";
        replyItem.textContent = reply.message;
        const replyMeta = document.createElement("span");
        replyMeta.textContent = `${reply.author} - ${formatDate(
          reply.createdAt
        )}`;
        replyItem.appendChild(replyMeta);
        replies.appendChild(replyItem);
      });

      const replyForm = document.createElement("form");
      replyForm.className = "forum-reply-form";
      replyForm.dataset.threadId = thread.id;

      const replyAuthorInput = document.createElement("input");
      replyAuthorInput.name = "replyAuthor";
      replyAuthorInput.type = "text";
      replyAuthorInput.placeholder = t("forumNamePlaceholder");
      replyAuthorInput.required = true;

      const replyInput = document.createElement("input");
      replyInput.name = "reply";
      replyInput.type = "text";
      replyInput.placeholder = t("forumReplyPlaceholder");
      replyInput.required = true;

      const replyButton = document.createElement("button");
      replyButton.type = "submit";
      replyButton.className = "secondary-btn";
      replyButton.textContent = t("forumReplyButton");

      replyForm.appendChild(replyAuthorInput);
      replyForm.appendChild(replyInput);
      replyForm.appendChild(replyButton);

      card.appendChild(title);
      card.appendChild(meta);
      card.appendChild(message);
      card.appendChild(replies);
      card.appendChild(replyForm);
      dom.forumThreads.appendChild(card);
    });
}

function handleTeacherSubmit(event) {
  event.preventDefault();
  const form = event.target;
  const payload = {
    id: `ex-${Date.now()}`,
    teacher: sanitize(form.teacherName.value),
    subject: sanitize(form.teacherSubject.value),
    level: sanitize(form.teacherLevel.value),
    theme: sanitize(form.teacherTheme.value),
    title: sanitize(form.teacherTitle.value),
    statement: sanitize(form.teacherStatement.value),
    solution: sanitize(form.teacherSolution.value),
    video: sanitize(form.teacherVideo.value),
    questions: [],
  };

  if (!payload.teacher || !payload.subject || !payload.level || !payload.title) {
    return;
  }

  state.exercises.push(payload);
  saveToStorage(STORAGE_KEYS.exercises, state.exercises);
  form.reset();
  dom.teacherStatus.textContent = t("teacherSuccess");
  window.setTimeout(() => {
    dom.teacherStatus.textContent = "";
  }, 2500);

  buildFilterOptions();
  renderTeacherExercises();
  renderExercises();
}

function handleQuestionSubmit(event) {
  const form = event.target.closest("form[data-exercise-id]");
  if (!form) return;
  event.preventDefault();
  const exerciseId = form.dataset.exerciseId;
  const author = sanitize(form.querySelector("[name='author']").value);
  const message = sanitize(form.querySelector("[name='message']").value);
  if (!author || !message) return;

  const exercise = state.exercises.find((item) => item.id === exerciseId);
  if (!exercise) return;

  exercise.questions.push({
    id: `q-${Date.now()}`,
    author,
    message,
    createdAt: new Date().toISOString(),
  });
  saveToStorage(STORAGE_KEYS.exercises, state.exercises);
  renderExercises();
}

function handleExerciseClick(event) {
  const toggleButton = event.target.closest("[data-action='toggle-solution']");
  if (toggleButton) {
    const card = toggleButton.closest(".exercise-card");
    const solution = card?.querySelector(".exercise-solution");
    if (solution) {
      solution.classList.toggle("is-hidden");
      const isHidden = solution.classList.contains("is-hidden");
      toggleButton.textContent = isHidden
        ? t("exerciseViewSolution")
        : t("exerciseHideSolution");
    }
  }

  const downloadButton = event.target.closest("[data-action='download']");
  if (downloadButton) {
    const exerciseId = downloadButton.dataset.exerciseId;
    const exercise = state.exercises.find((item) => item.id === exerciseId);
    if (exercise) {
      downloadExercise(exercise);
    }
  }
}

function handleChatbotSubmit(event) {
  event.preventDefault();
  const message = sanitize(dom.chatbotInput.value);
  if (!message) return;
  dom.chatbotInput.value = "";
  addChatMessage("user", message);

  const response = getChatbotResponse(message);
  addChatMessage("bot", response);
  saveToStorage(STORAGE_KEYS.chat, state.chatHistory);
  renderChatbot();
}

function handleForumSubmit(event) {
  event.preventDefault();
  const form = event.target;
  const payload = {
    id: `thread-${Date.now()}`,
    author: sanitize(form.forumName.value),
    subject: sanitize(form.forumSubject.value),
    level: sanitize(form.forumLevel.value),
    message: sanitize(form.forumMessage.value),
    createdAt: new Date().toISOString(),
    replies: [],
  };

  if (!payload.author || !payload.subject || !payload.level || !payload.message) {
    return;
  }

  state.forumThreads.push(payload);
  saveToStorage(STORAGE_KEYS.forum, state.forumThreads);
  form.reset();
  renderForumThreads();
}

function handleForumReplySubmit(event) {
  const form = event.target.closest("form[data-thread-id]");
  if (!form) return;
  event.preventDefault();
  const threadId = form.dataset.threadId;
  const replyAuthor = sanitize(
    form.querySelector("input[name='replyAuthor']").value
  );
  const replyText = sanitize(form.querySelector("input[name='reply']").value);
  if (!replyAuthor || !replyText) return;

  const thread = state.forumThreads.find((item) => item.id === threadId);
  if (!thread) return;

  thread.replies.push({
    id: `reply-${Date.now()}`,
    author: replyAuthor,
    message: replyText,
    createdAt: new Date().toISOString(),
  });
  saveToStorage(STORAGE_KEYS.forum, state.forumThreads);
  renderForumThreads();
}

function addChatMessage(from, text) {
  state.chatHistory.push({ from, text });
}

function ensureChatWelcome() {
  if (state.chatHistory.length === 0) {
    addChatMessage("bot", t("chatbotWelcome"));
    addChatMessage("bot", t("chatbotSuggestion"));
    saveToStorage(STORAGE_KEYS.chat, state.chatHistory);
  }
}

function getChatbotResponse(message) {
  const query = message.toLowerCase();
  const filters = getFilters();

  if (query.includes("bonjour") || query.includes("salut")) {
    return t("chatbotWelcome");
  }

  if (query.includes("video")) {
    const withVideos = state.exercises.filter((item) => item.video);
    return withVideos.length
      ? `${t("exerciseVideo")}: ${withVideos
          .slice(0, 3)
          .map((item) => item.title)
          .join(", ")}.`
      : t("exerciseNoResults");
  }

  if (query.includes("corrige") || query.includes("solution")) {
    return t("exerciseViewSolution");
  }

  if (query.includes("forum")) {
    return t("forumSubtitle");
  }

  if (query.includes("exercice") || query.includes("exercise")) {
    const suggested = suggestExercises(filters.level);
    return suggested.length
      ? `Suggestions: ${suggested.join(", ")}.`
      : t("exerciseNoResults");
  }

  return t("chatbotSuggestion");
}

function suggestExercises(level) {
  const pool =
    level && level !== "all"
      ? state.exercises.filter((item) => item.level === level)
      : state.exercises;
  return pool.slice(0, 3).map((item) => item.title);
}

function getFilters() {
  return {
    subject: dom.filterSubject?.value || "all",
    level: dom.filterLevel?.value || "all",
    theme: dom.filterTheme?.value || "all",
    search: dom.filterSearch?.value.trim().toLowerCase() || "",
  };
}

function uniqueValues(values) {
  return Array.from(new Set(values.filter(Boolean))).sort((a, b) =>
    a.localeCompare(b)
  );
}

function formatDate(isoDate) {
  try {
    return new Date(isoDate).toLocaleDateString();
  } catch (error) {
    return isoDate;
  }
}

function sanitize(value) {
  if (!value) return "";
  return value.toString().trim().slice(0, 400);
}

function downloadExercise(exercise) {
  const content = [
    exercise.title,
    `Matiere: ${exercise.subject}`,
    `Niveau: ${exercise.level}`,
    `Theme: ${exercise.theme}`,
    "",
    exercise.statement,
    "",
    `Corrige: ${exercise.solution || "Non fourni"}`,
  ].join("\n");

  const blob = new Blob([content], { type: "text/plain" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = `${exercise.title.replace(/\s+/g, "_")}.txt`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(link.href);
}
