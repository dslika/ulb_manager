<template>
  <div>
    <!-- Standard -->
    <b-card header="Header"
            class="mb-2"
            title="Doc page"
            sub-title="sample page"
            show-footer>

      <ul>
        <li v-for='item in gridData'>{{item.id}} : {{item.title}} : {{item.stock_count}}</li>
      </ul>

      <small slot="footer" class="text-muted">
        Doc
      </small>
    </b-card>
  </div>
</template>

<script>
  export default {
    name: 'main',
    data () {
      return {
        searchQuery: '',
        gridColumns: ['id', 'title', 'stock_count'], // 変更
        gridData: [] // データはAPIで取ってくるので削除
      }
    },

    created: function () {
      let self = this
      this.axios.get('http://0.0.0.0:8000/qiita/api/stock/').then((response) => {
        self.gridData = response.data
      }).catch((response) => {
        self.console.log(response)
      })
    }
  }
</script>
