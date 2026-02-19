<template>
  <q-page class="flex flex-center q-pa-md">
    <div style="width: 100%; max-width: 600px">

      <q-form @submit.prevent="handleSend" class="row q-col-gutter-sm q-mb-lg">
        <div class="col">
          <q-input
            v-model="newItemText"
            outlined
            dense
            label="Текст новой записи"
            :disable="sending"
          />
        </div>
        <div class="col-auto">
          <q-btn type="submit" color="primary" icon="send" :loading="sending" />
        </div>
      </q-form>

      <q-card flat bordered class="column shadow-2">
        <q-toolbar class="bg-primary text-white">
          <q-toolbar-title>Элементы ({{ itemStore.items.length }})</q-toolbar-title>
          <q-btn flat round icon="refresh" @click="resetList" />
        </q-toolbar>

        <!-- Контейнер со скроллом -->
        <div class="overflow-auto" style="max-height: 500px;">
          <q-infinite-scroll
            ref="infiniteRef"
            @load="onLoadMore"
            :offset="150"
          >
            <q-list separator>
              <q-item v-for="item in itemStore.items" :key="item?.id">
                <q-item-section>
                  <q-item-label class="text-weight-bold">{{ item?.text }}</q-item-label>
                  <q-item-label caption>ID: {{ item?.id }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>

            <template v-slot:loading>
              <div class="row justify-center q-my-md">
                <q-spinner-dots color="primary" size="40px" />
              </div>
            </template>
          </q-infinite-scroll>

          <div v-if="!itemStore.nextCursor && itemStore.items.length > 0" class="text-center q-pa-md text-grey italic">
            Данных больше нет
          </div>
        </div>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useItemStore } from 'src/store/items'

const itemStore = useItemStore()
const newItemText = ref('')
const sending = ref(false)
const infiniteRef = ref(null)

const onLoadMore = async (index, done) => {
  const isLoadMore = index > 1
  const cursorAfterUpdate = await itemStore.fetchItems(isLoadMore)

  if (cursorAfterUpdate === null) {
    done(true)
  } else {
    done()
  }
}

const resetList = async () => {
  itemStore.items = []
  if (infiniteRef.value) {
    infiniteRef.value.reset()
    infiniteRef.value.resume()
    infiniteRef.value.trigger()
  }
}

const handleSend = async () => {
  const text = newItemText.value.trim()
  if (!text) return

  sending.value = true
  try {
    await itemStore.addItem(text)
    newItemText.value = ''
  } finally {
    sending.value = false
  }
}
</script>