<script>
export let page=1
export let selectPage
export let pageNumbers
export let maxPage


</script>

<style>
.active {
  background-color: blue;
  color: white;
}
</style>


      
      <nav class="py-5" aria-label="...">
        <ul class="pagination">
        {#if page>2}
          <li class="page-item"  on:click={() => selectPage(page-2)}>
            <a class="page-link" href="#">&laquo;</a>
          </li>
        {/if}
        {#each pageNumbers as pageNumber}
          <li class="page-item"  on:click={() => selectPage(pageNumber)}>
            <a class="page-link" class:active={pageNumber===page} href="#">{pageNumber}</a>
          </li>
        {/each}
        {#if page<maxPage-1}
          <li class="page-item"  on:click={() => selectPage(page+2)}>
            <a class="page-link" href="#">&raquo;</a>
          </li>
        {/if}
        </ul>
    </nav>
