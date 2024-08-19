
import prisma from './db.js';

async function main() {
  const newUser = await prisma.user.create({
    data: {
      name: 'Alexandre',
      email: 'Alexandre@example.com',
      password: 'admin123',
    },
  });

  console.log('Novo usuário criado:', newUser);

  const users = await prisma.user.findMany();
  console.log('Todos os usuários:', users);
}

main()
  .catch(e => console.error(e))
  .finally(async () => {
    await prisma.$disconnect();
  });
