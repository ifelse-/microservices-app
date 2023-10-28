import { Subjects, Publisher, PaymentCreatedEvent } from '@scriptmotor/common';

export class PaymentCreatedPublisher extends Publisher<PaymentCreatedEvent> {
  subject: Subjects.PaymentCreated = Subjects.PaymentCreated;
}
