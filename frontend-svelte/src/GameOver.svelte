<script>
export let numCorrect
export let totalQuestions
export let newGame

</script>

<style>
h3{
    color:rgb(192, 30, 30)(144, 68, 68);
}

</style>

<h3 class="alert alert-success">You got {numCorrect} from {totalQuestions} ! 
<img width="100px" src="flowers.png" alt="flower">
</h3>
<button on:click={newGame} class="btn btn-success my-3">New Game ?</button>
