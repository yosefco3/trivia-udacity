<script>
import { Router, link, Route } from "svelte-routing";
import QuestionView from './QuestionView.svelte'
import FormView from './FormView.svelte'
import QuizView from './QuizView.svelte'



let url = "localhost:5000";
</script>

<style>
img{
  width:50px;
}
.navbar {
  margin: 0;
}

</style>


<Router url="{url}">
  <nav class="navbar navbar-expand-lg navbar-light my-0" style="background-color: #e3f2fd;">
  <div class="navbar-brand" href="/" use:link><img src="favicon.png" alt="trivia"></div>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="/" use:link>Home<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/add" use:link>Add Question</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/play" use:link>Play</a>
      </li>
    </ul>
  </div>
</nav>


  <Route path="/" component={QuestionView} />
  <Route path="/add" component={FormView} />
  <Route path="/play" component={QuizView} />
  <Route component={QuestionView} />
</Router>
