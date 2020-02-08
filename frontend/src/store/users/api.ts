import { client } from '@/store/api'

import { User } from '@/@types/users';

export async function checkEmailExists(email: string): Promise<{ email: string }> {
  const response = await client.get(`users/${email}/exists/`)
  return response.data
}

export async function getCurrentUser(): Promise<User> {
  const response = await client.get(`users/current/`)
  return response.data
}

export async function updateUserPassword(password: string): Promise<User> {
  const response = await client.put(`users/current/set_password/`, { password })
  return response.data
}