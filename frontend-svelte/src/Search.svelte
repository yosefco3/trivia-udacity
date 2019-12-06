<script>
let query=""
export let submitSearch

let handleSubmit=()=>{
    submitSearch(query)
}
</script>

<style>
form {
    margin-top: 20px;
}

</style>

<form on:submit|preventDefault={handleSubmit}>
    <input placeholder="Search questions..." bind:value={query}/>
    <button type="submit" class="btn btn-danger">Search</button>
</form>
