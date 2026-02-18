import { defineStore } from 'pinia'
import axios from 'axios'

const api = axios.create({ baseURL: 'http://localhost:8000' })

export const useItemStore = defineStore('items', {
  state: () => ({
    items: [],
    nextCursor: null,
    loading: false
  }),

  actions: {
    async fetchItems(isLoadMore = false) {
      if (this.loading) return

      this.loading = true
      try {
        const params = {}
        if (isLoadMore && this.nextCursor) {
          params.next_cursor = this.nextCursor
        }

        const response = await api.get('/api/items', { params })
        const { items, next_cursor } = response.data

        if (isLoadMore) {
          const newItems = items.filter(newItem => !this.items.find(i => i.id === newItem.id))
          this.items.push(...newItems)
        } else {
          this.items = items
        }

        this.nextCursor = next_cursor
        return next_cursor
      } catch (error) {
        console.error('Ошибка загрузки:', error)
        return null
      } finally {
        this.loading = false
      }
    },

    async addItem(text) {
      try {
        const response = await api.post('/api/items', { text })
        if (response.data) {
          this.items.unshift(response.data)
        }
      } catch (error) {
        console.error('Ошибка добавления:', error)
        throw error
      }
    }
  }
})