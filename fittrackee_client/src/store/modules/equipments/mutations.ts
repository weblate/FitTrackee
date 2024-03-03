import type { MutationTree } from 'vuex'

import { EQUIPMENTS_STORE } from '@/store/constants'
import type {
  IEquipmentTypesState,
  TEquipmentsMutations,
} from '@/store/modules/equipments/types'
import type { IEquipment, IEquipmentType } from '@/types/equipments'

export const mutations: MutationTree<IEquipmentTypesState> &
  TEquipmentsMutations = {
  [EQUIPMENTS_STORE.MUTATIONS.REMOVE_EQUIPMENT](
    state: IEquipmentTypesState,
    equipmentId: number
  ) {
    const equipmentIndex = state.equipments.findIndex(
      (e) => e.id === equipmentId
    )
    delete state.equipments[equipmentIndex]
  },
  [EQUIPMENTS_STORE.MUTATIONS.SET_EQUIPMENT](
    state: IEquipmentTypesState,
    equipment: IEquipment
  ) {
    const equipmentIndex = state.equipments.findIndex(
      (e) => e.id === equipment.id
    )
    if (equipmentIndex !== -1) {
      state.equipments[equipmentIndex] = equipment
    }
  },
  [EQUIPMENTS_STORE.MUTATIONS.SET_EQUIPMENTS](
    state: IEquipmentTypesState,
    equipments: IEquipment[]
  ) {
    state.equipments = equipments
  },
  [EQUIPMENTS_STORE.MUTATIONS.SET_EQUIPMENT_TYPES](
    state: IEquipmentTypesState,
    equipmentTypes: IEquipmentType[]
  ) {
    state.equipmentTypes = equipmentTypes
  },
}
