-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "email" TEXT NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Pacientes" (
    "id" SERIAL NOT NULL,
    "nome" TEXT NOT NULL,
    "numAcesso" TEXT NOT NULL,
    "visita" TEXT NOT NULL,
    "patientID" TEXT NOT NULL,
    "data" TIMESTAMP(3) NOT NULL,
    "modalidade" TEXT NOT NULL,
    "tipoExame" TEXT NOT NULL,
    "numero" TEXT NOT NULL,
    "estado" TEXT NOT NULL,
    "medSol" TEXT NOT NULL,
    "laudo" TEXT NOT NULL,
    "sexo" TEXT NOT NULL,
    "especial" TEXT NOT NULL,
    "urgente" TEXT NOT NULL,
    "restaurado" TEXT NOT NULL,

    CONSTRAINT "Pacientes_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Pacientes_patientID_key" ON "Pacientes"("patientID");

-- CreateIndex
CREATE UNIQUE INDEX "Pacientes_numero_key" ON "Pacientes"("numero");
